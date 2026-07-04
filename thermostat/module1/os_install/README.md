# Installing the OS

Here we will be installing the OS onto the 
Raspberry Pi.

## Instructions

Check the options on the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) they should be similar to the image
below. 

<figure>
  <img src="../../images/module1/os_install/16_app_options.png" alt="App Options" width="400" />
</figure>


1. Insert the card reader into the USB port on your computer and open the software

2. We start on the Device step

<figure>
  <img src="../../images/module1/os_install/1_device_screen.png" alt="Device Select" width="400" />
</figure>


3. Choose the Raspberry Pi 4 and click NEXT

<figure>
  <img src="../../images/module1/os_install/2_raspberry_pi_4_select.png" alt="Select Raspberry Pi" width="400" />
</figure>


4. On the OS step, go to Other general-purpose OS

<figure>
  <img src="../../images/module1/os_install/3_general_purpose_os.png" alt="General Purpose OS" width="400" />
</figure>


5. Choose Ubuntu for the Operating System

<figure>
  <img src="../../images/module1/os_install/4_choose_ubuntu.png" alt="Choose Ubuntu" width="400" />
</figure>

6. Choose Ubuntu Server 24.04.4 LTS (64-bit) and click NEXT

<figure>
  <img src="../../images/module1/os_install/5_ubuntu_server.png" alt="Ubuntu Server" width="400" />
</figure>

7. Select the device (and make sure it is the correct one)

<figure>
  <img src="../../images/module1/os_install/6_choose_storage.png" alt="Choose Storage" width="400" />
</figure>

8. Set a hostname, here I am using cs350labpi4

<figure>
  <img src="../../images/module1/os_install/7_enter_hostname.png" alt="Enter Hostname" width="400" />
</figure>

9. Set the capital city, time zone, and keyboard layout

<figure>
  <img src="../../images/module1/os_install/8_localisation.png" alt="Localisation" width="400" />
</figure>

10. Set your username and password

<figure>
  <img src="../../images/module1/os_install/9_choose_username.png" alt="Choose Username" width="400" />
</figure>

11. Set your WIFI options

<figure>
  <img src="../../images/module1/os_install/10_choose_wifi.png" alt="Choose WiFi" width="400" />
</figure>

12. Ensure Enable SSH is set and that you are using "Use password authentication".  Click NEXT.

<figure>
  <img src="../../images/module1/os_install/11_ssh_auth.png" alt="SSH Auth" width="400" />
</figure>

13. We are now ready to write the image, doublecheck you configured options and click WRITE

<figure>
  <img src="../../images/module1/os_install/12_write_image.png" alt="Write Image" width="400" />
</figure>

14. Again make sure you have the write drive and then write the image.

<figure>
  <img src="../../images/module1/os_install/13_about_to_erase_drive.png" alt="About to Erase Drive" width="400" />
</figure>

15. The image begins writing, the process can be a bit slow sometimes

<figure>
  <img src="../../images/module1/os_install/14_writing_image.png" alt="Writing Image" width="400" />
</figure>

16. After writing the image, it will be verified.

<figure>
  <img src="../../images/module1/os_install/15_verifying_image.png" alt="Verifying Image" width="400" />
</figure>

17. It took about 8 minutes to complete the process.

<figure>
  <img src="../../images/module1/os_install/17_complete.png" alt="Complete" width="400" />
</figure>

You should be able to continue with the rest of the lab instructions
