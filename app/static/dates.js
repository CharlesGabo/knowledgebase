(function(root){
 const dateValue=s=>new Date(s+'T12:00:00Z');
 const iso=d=>d.toISOString().slice(0,10);
 function shift(s,n){const d=dateValue(s);d.setUTCDate(d.getUTCDate()+n);return iso(d)}
 function monday(s){return shift(s,-((dateValue(s).getUTCDay()+6)%7))}
 function periodRange(period,selected){if(period==='all')return null;if(period==='day')return[selected,selected];if(period==='week'){const a=monday(selected);return[a,shift(a,6)]}const d=dateValue(selected);return[iso(new Date(Date.UTC(d.getUTCFullYear(),d.getUTCMonth(),1,12))),iso(new Date(Date.UTC(d.getUTCFullYear(),d.getUTCMonth()+1,0,12)))]}
 function reschedule(task,start){const days=task.start&&task.end?Math.round((dateValue(task.end)-dateValue(task.start))/86400000):0;return {start,end:days?shift(start,days):null}}
 const api={dateValue,iso,shift,monday,periodRange,reschedule};
 if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.TaskDates=api;
})(globalThis);
