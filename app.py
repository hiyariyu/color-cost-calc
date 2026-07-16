import { useState } from "react";

export default function App() {
  const [a1g, setA1g] = useState(120);
  const [a1price, setA1price] = useState(360);
  const [a2g, setA2g] = useState(2000);
  const [a2price, setA2price] = useState(1000);
  const [ratio1, setRatio1] = useState(1);
  const [ratio2, setRatio2] = useState(2);

  const unit1 = a1price / a1g;
  const unit2 = a2price / a2g;

  const mixed =
    (unit1 * ratio1 + unit2 * ratio2) /
    (ratio1 + ratio2);

  return (
    <div style={{padding:20}}>
      <h2>カラー価格比較</h2>

      <p>1剤容量</p>
      <input
        type="number"
        value={a1g}
        onChange={(e)=>setA1g(Number(e.target.value))}
      />

      <p>1剤価格</p>
      <input
        type="number"
        value={a1price}
        onChange={(e)=>setA1price(Number(e.target.value))}
      />

      <p>2剤容量</p>
      <input
        type="number"
        value={a2g}
        onChange={(e)=>setA2g(Number(e.target.value))}
      />

      <p>2剤価格</p>
      <input
        type="number"
        value={a2price}
        onChange={(e)=>setA2price(Number(e.target.value))}
      />

      <p>混合比</p>
      <input
        type="number"
        value={ratio1}
        onChange={(e)=>setRatio1(Number(e.target.value))}
      />
      :
      <input
        type="number"
        value={ratio2}
        onChange={(e)=>setRatio2(Number(e.target.value))}
      />

      <hr/>

      <h3>1剤単価：{unit1.toFixed(2)} 円/g</h3>
      <h3>2剤単価：{unit2.toFixed(2)} 円/g</h3>
      <h2>混合後単価：{mixed.toFixed(2)} 円/g</h2>
    </div>
  );
}
