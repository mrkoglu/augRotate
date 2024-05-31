<h1>Proje Açıklaması</h1>

<p>
    Bu Python betiği, belirli bir klasördeki JPG ve TXT dosyalarını işleyerek yeni bir klasöre kopyalar. Betik, JPG dosyalarını belirli bir açıda döndürür ve döndürülmüş dosyaları yeni bir klasöre kaydeder. Aynı klasördeki TXT dosyalarını okuyarak belirli koordinatları döndürülen görüntüye göre günceller ve bu güncellenmiş koordinatları yeni bir klasöre kaydeder.
</p>

<h2>Kod Açıklaması</h2>
<ul>
    <li><code>show(image, title="Image")</code>: Görüntüyü görselleştirmek için matplotlib kullanır.</li>
    <li><code>read_txt(filename)</code>: TXT dosyasından sınıf ve koordinat bilgilerini okur.</li>
    <li><code>rotate_image(image, angle)</code>: Görüntüyü belirtilen açıda döndürür.</li>
    <li><code>find_rotated_bbox(coord, rotated_mask)</code>: Döndürülen maske üzerinde sınırlayıcı kutuyu bulur.</li>
</ul>

<h2>Nasıl Kullanılır?</h2>
<ol>
<li><strong>Gereksinimler</strong>
    <ul>
        <li>Python 3.x</li>
        <li>OpenCV</li>
        <li>NumPy</li>
        <li>Matplotlib</li>
    </ul>
</li>

<li><strong>Kurulum</strong>
    <pre><code>pip install opencv-python numpy matplotlib</code></pre>
</li>

<li><strong>Kod Açıklaması</strong>
    <p>Betiği çalıştırmadan önce <code>ornek_resimler</code> klasörüne işlem yapılacak JPG ve TXT dosyalarını yerleştirin.</p>
    <p>Script dosyasını çalıştırdıktan sonra <code>output</code> klasöründe işlenmiş dosyaları gözlemleyin.</p>
</li>

<li><strong>Örnek Kullanım</strong>
    <pre><code>python script.py</code></pre>
</li>
</ol>

<h2>Lisans</h2>
<p>Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için <a href="./LICENSE">LICENSE</a> dosyasına göz atabilirsiniz.</p>
