const test=require('node:test');
const assert=require('node:assert/strict');
const {shift,monday,periodRange,reschedule}=require('../static/dates.js');
test('Monday through Sunday including year boundary',()=>{assert.deepEqual(periodRange('week','2027-01-01'),['2026-12-28','2027-01-03']);assert.equal(monday('2026-11-16'),'2026-11-16')});
test('month handles leap years and December',()=>{assert.deepEqual(periodRange('month','2028-02-12'),['2028-02-01','2028-02-29']);assert.deepEqual(periodRange('month','2026-12-31'),['2026-12-01','2026-12-31'])});
test('day and all ranges',()=>{assert.deepEqual(periodRange('day','2026-11-16'),['2026-11-16','2026-11-16']);assert.equal(periodRange('all','2026-11-16'),null)});
test('date arithmetic survives month boundary',()=>{assert.equal(shift('2026-11-30',1),'2026-12-01');assert.equal(shift('2026-01-01',-1),'2025-12-31')});
test('calendar drag preserves inclusive duration without touching deadline',()=>{const task={start:'2026-11-16',end:'2026-11-18',deadline:'2026-12-01'};assert.deepEqual(reschedule(task,'2026-11-30'),{start:'2026-11-30',end:'2026-12-02'});assert.equal(task.deadline,'2026-12-01')});
test('unscheduled card becomes single day',()=>{assert.deepEqual(reschedule({start:null,end:null},'2026-11-16'),{start:'2026-11-16',end:null})});
