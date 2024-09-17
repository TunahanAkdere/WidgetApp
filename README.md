# **Currency Exchange Widget 💱**

## **English**

This project is a simple Tkinter-based application that automatically fetches the current exchange rates (USD and EUR) in Turkey and displays them in a user-friendly interface. 🌍📊 The data is fetched from doviz.com and is updated every minute. 🔄

## **Features**

- **USD and EUR Rates**: Displays the current exchange rates for USD and EUR. 💵💶
- **Automatic Updates**: Exchange rates are refreshed every 60 seconds. ⏲️
- **Last Update Time**: Shows the last time the rates were updated. 📅
- **Single Executable Output**: A standalone EXE file can be created using PyInstaller. 🏆

## **Requirements**

- `requests` 📦
- `beautifulsoup4` 📦
- `PyInstaller` (for creating an EXE) 🛠️
- `tkinter` (included with Python as a GUI library) ⚙️

## **Usage**

### **Setup**

1. **Clone or Download the Repository**: 
   - Use the following command to clone the repository to your local machine:
     ```bash
     git clone https://github.com/your-username/CurrencyExchangeWidget.git
     ```
   - Alternatively, you can download the ZIP file from the repository page and extract it to your desired location. 📂

2. **Navigate to the Project Directory**: 
   - Open your terminal or command prompt and change to the project directory:
     ```bash
     cd CurrencyExchangeWidget
     ```

3. **Install Required Dependencies**:
   - Install the necessary Python libraries using pip:
     ```bash
     pip install requests beautifulsoup4 pyinstaller
     ```
   - Ensure that Python is installed on your system. You can check this by running `python --version`. If Python is not installed, download and install it from the [official Python website](https://www.python.org/downloads/). 🧑‍💻

### **Running the Application**

1. **Run the Application**:
   - Execute the following command to start the application:
     ```bash
     python WidgetCurrency.py
     ```
   - The Tkinter window should open, displaying the current USD and EUR exchange rates. 🌐

2. **Using the Application**:
   - The application will automatically fetch and display the exchange rates for USD and EUR. 💵💶
   - The exchange rates will be updated every 60 seconds. ⏲️
   - The last update time will be shown on the interface. 📅

### **Building the Executable**

1. **Create the Executable File**:
   - Use PyInstaller to package the application into a standalone executable. Run the following command:
     ```bash
     python WidgetCurrency.py --build
     ```
   - PyInstaller will generate an executable file in the `dist` directory. 📦

2. **Distribute and Run the Executable**:
   - You can now distribute the executable file to others. It does not require Python to be installed on the target machine.
   - Double-click the EXE file to run the application, and it should function just like the Python script. 🖥️

## **Türkçe**

Bu proje, Türkiye'deki güncel döviz kurlarını (USD ve EUR) otomatik olarak çeken ve kullanıcı dostu bir arayüzde gösteren basit bir Tkinter tabanlı uygulamadır. 🌍📊 Veriler doviz.com web sitesinden çekilir ve her dakika güncellenir. 🔄

## **Özellikler**

- **USD ve EUR Kurları**: Güncel USD ve EUR döviz kurlarını gösterir. 💵💶
- **Otomatik Güncelleme**: Döviz kurları her 60 saniyede bir otomatik olarak yenilenir. ⏲️
- **Son Güncelleme Saati**: Kurların en son güncellendiği zamanı gösterir. 📅
- **Tek Dosya Çıktısı**: PyInstaller ile tek bir EXE dosyası oluşturulabilir. 🏆

## **Gereksinimler**

- `requests` 📦
- `beautifulsoup4` 📦
- `PyInstaller` (EXE oluşturmak için) 🛠️
- `tkinter` (Python ile birlikte gelen GUI kütüphanesi) ⚙️

## **Kullanım**

### **Kurulum**

1. **Projeyi Klonlayın veya İndirin**:
   - Aşağıdaki komutu kullanarak projeyi yerel makinenize klonlayın:
     ```bash
     git clone https://github.com/your-username/CurrencyExchangeWidget.git
     ```
   - Alternatif olarak, GitHub'dan ZIP dosyasını indirebilir ve istediğiniz konuma çıkarabilirsiniz. 📂

2. **Proje Dizini'ne Geçin**:
   - Terminal veya komut istemcisini açın ve proje dizinine geçin:
     ```bash
     cd CurrencyExchangeWidget
     ```

3. **Gerekli Bağımlılıkları Yükleyin**:
   - Gerekli Python kütüphanelerini pip kullanarak yükleyin:
     ```bash
     pip install requests beautifulsoup4 pyinstaller
     ```
   - Python'un sisteminizde kurulu olduğundan emin olun. Kurulu olup olmadığını `python --version` komutuyla kontrol edebilirsiniz. Python kurulu değilse, [resmi Python web sitesinden](https://www.python.org/downloads/) indirip yükleyin. 🧑‍💻

### **Uygulamayı Çalıştırma**

1. **Uygulamayı Çalıştırın**:
   - Uygulamayı başlatmak için aşağıdaki komutu çalıştırın:
     ```bash
     python WidgetCurrency.py
     ```
   - Tkinter penceresi açılacak ve güncel USD ve EUR döviz kurları gösterilecektir. 🌐

2. **Uygulamayı Kullanma**:
   - Uygulama otomatik olarak USD ve EUR döviz kurlarını çekecek ve gösterecektir. 💵💶
   - Döviz kurları her 60 saniyede bir güncellenecektir. ⏲️
   - Son güncelleme saati arayüzde gösterilecektir. 📅

### **Çalıştırılabilir Dosyayı Oluşturma**

1. **Çalıştırılabilir Dosya Oluşturun**:
   - PyInstaller kullanarak uygulamayı bağımsız bir çalıştırılabilir dosya olarak paketleyin. Aşağıdaki komutu çalıştırın:
     ```bash
     python WidgetCurrency.py --build
     ```
   - PyInstaller, `dist` dizininde bir çalıştırılabilir dosya oluşturacaktır. 📦

2. **Çalıştırılabilir Dosyayı Dağıtın ve Çalıştırın**:
   - Artık çalıştırılabilir dosyayı başkalarına dağıtabilirsiniz. Hedef makinede Python'un kurulu olmasını gerektirmez.
   - EXE dosyasına çift tıklayarak uygulamayı çalıştırabilirsiniz ve Python betiği gibi çalışacaktır. 🖥️
