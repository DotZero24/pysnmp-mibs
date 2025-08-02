_G='endptRASGkEntryData'
_F='endptResetLogText'
_E='endptRecentLogText'
_D='Avaya-46xxIPTelephone-MIB'
_C='obsolete'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
endpointMIB=ModuleIdentity((1,3,6,1,4,1,6889,2,69,1))
_Avaya_ObjectIdentity=ObjectIdentity
avaya=_Avaya_ObjectIdentity((1,3,6,1,4,1,6889))
_AvayaProducts_ObjectIdentity=ObjectIdentity
avayaProducts=_AvayaProducts_ObjectIdentity((1,3,6,1,4,1,6889,1))
_AvayaipEndpointProd_ObjectIdentity=ObjectIdentity
avayaipEndpointProd=_AvayaipEndpointProd_ObjectIdentity((1,3,6,1,4,1,6889,1,69))
_AvayaMibs_ObjectIdentity=ObjectIdentity
avayaMibs=_AvayaMibs_ObjectIdentity((1,3,6,1,4,1,6889,2))
_AvayaipEndpointMIBs_ObjectIdentity=ObjectIdentity
avayaipEndpointMIBs=_AvayaipEndpointMIBs_ObjectIdentity((1,3,6,1,4,1,6889,2,69))
_EndptID_ObjectIdentity=ObjectIdentity
endptID=_EndptID_ObjectIdentity((1,3,6,1,4,1,6889,2,69,1,1))
_EndptMARKET_Type=DisplayString
_EndptMARKET_Object=MibScalar
endptMARKET=_EndptMARKET_Object((1,3,6,1,4,1,6889,2,69,1,1,1),_EndptMARKET_Type())
endptMARKET.setMaxAccess(_A)
if mibBuilder.loadTexts:endptMARKET.setStatus(_C)
_EndptMODEL_Type=DisplayString
_EndptMODEL_Object=MibScalar
endptMODEL=_EndptMODEL_Object((1,3,6,1,4,1,6889,2,69,1,1,2),_EndptMODEL_Type())
endptMODEL.setMaxAccess(_A)
if mibBuilder.loadTexts:endptMODEL.setStatus(_B)
_EndptMCIPADD_Type=DisplayString
_EndptMCIPADD_Object=MibScalar
endptMCIPADD=_EndptMCIPADD_Object((1,3,6,1,4,1,6889,2,69,1,1,3),_EndptMCIPADD_Type())
endptMCIPADD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptMCIPADD.setStatus(_B)
_EndptMCIPINUSE_Type=IpAddress
_EndptMCIPINUSE_Object=MibScalar
endptMCIPINUSE=_EndptMCIPINUSE_Object((1,3,6,1,4,1,6889,2,69,1,1,4),_EndptMCIPINUSE_Type())
endptMCIPINUSE.setMaxAccess(_A)
if mibBuilder.loadTexts:endptMCIPINUSE.setStatus(_B)
_EndptMCPORT_Type=Integer32
_EndptMCPORT_Object=MibScalar
endptMCPORT=_EndptMCPORT_Object((1,3,6,1,4,1,6889,2,69,1,1,5),_EndptMCPORT_Type())
endptMCPORT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptMCPORT.setStatus(_B)
_EndptPHONESN_Type=DisplayString
_EndptPHONESN_Object=MibScalar
endptPHONESN=_EndptPHONESN_Object((1,3,6,1,4,1,6889,2,69,1,1,6),_EndptPHONESN_Type())
endptPHONESN.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPHONESN.setStatus(_B)
_EndptPWBCC_Type=DisplayString
_EndptPWBCC_Object=MibScalar
endptPWBCC=_EndptPWBCC_Object((1,3,6,1,4,1,6889,2,69,1,1,7),_EndptPWBCC_Type())
endptPWBCC.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPWBCC.setStatus(_B)
_EndptPWBSN_Type=DisplayString
_EndptPWBSN_Object=MibScalar
endptPWBSN=_EndptPWBSN_Object((1,3,6,1,4,1,6889,2,69,1,1,8),_EndptPWBSN_Type())
endptPWBSN.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPWBSN.setStatus(_B)
_EndptETHERADD_Type=OctetString
_EndptETHERADD_Object=MibScalar
endptETHERADD=_EndptETHERADD_Object((1,3,6,1,4,1,6889,2,69,1,1,9),_EndptETHERADD_Type())
endptETHERADD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptETHERADD.setStatus(_B)
_EndptESPEED_Type=DisplayString
_EndptESPEED_Object=MibScalar
endptESPEED=_EndptESPEED_Object((1,3,6,1,4,1,6889,2,69,1,1,10),_EndptESPEED_Type())
endptESPEED.setMaxAccess(_A)
if mibBuilder.loadTexts:endptESPEED.setStatus(_B)
_EndptIPADD_Type=IpAddress
_EndptIPADD_Object=MibScalar
endptIPADD=_EndptIPADD_Object((1,3,6,1,4,1,6889,2,69,1,1,11),_EndptIPADD_Type())
endptIPADD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptIPADD.setStatus(_B)
_EndptDHCPLEASETIME_Type=Integer32
_EndptDHCPLEASETIME_Object=MibScalar
endptDHCPLEASETIME=_EndptDHCPLEASETIME_Object((1,3,6,1,4,1,6889,2,69,1,1,12),_EndptDHCPLEASETIME_Type())
endptDHCPLEASETIME.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDHCPLEASETIME.setStatus(_B)
_EndptDHCPLEASERENEW_Type=Integer32
_EndptDHCPLEASERENEW_Object=MibScalar
endptDHCPLEASERENEW=_EndptDHCPLEASERENEW_Object((1,3,6,1,4,1,6889,2,69,1,1,13),_EndptDHCPLEASERENEW_Type())
endptDHCPLEASERENEW.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDHCPLEASERENEW.setStatus(_B)
_EndptDHCPLEASEREBIND_Type=Integer32
_EndptDHCPLEASEREBIND_Object=MibScalar
endptDHCPLEASEREBIND=_EndptDHCPLEASEREBIND_Object((1,3,6,1,4,1,6889,2,69,1,1,14),_EndptDHCPLEASEREBIND_Type())
endptDHCPLEASEREBIND.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDHCPLEASEREBIND.setStatus(_B)
_EndptGIPADD_Type=DisplayString
_EndptGIPADD_Object=MibScalar
endptGIPADD=_EndptGIPADD_Object((1,3,6,1,4,1,6889,2,69,1,1,15),_EndptGIPADD_Type())
endptGIPADD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptGIPADD.setStatus(_B)
_EndptGIPINUSE_Type=IpAddress
_EndptGIPINUSE_Object=MibScalar
endptGIPINUSE=_EndptGIPINUSE_Object((1,3,6,1,4,1,6889,2,69,1,1,16),_EndptGIPINUSE_Type())
endptGIPINUSE.setMaxAccess(_A)
if mibBuilder.loadTexts:endptGIPINUSE.setStatus(_B)
_EndptNETMASK_Type=IpAddress
_EndptNETMASK_Object=MibScalar
endptNETMASK=_EndptNETMASK_Object((1,3,6,1,4,1,6889,2,69,1,1,17),_EndptNETMASK_Type())
endptNETMASK.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNETMASK.setStatus(_B)
_EndptTFTPDIR_Type=DisplayString
_EndptTFTPDIR_Object=MibScalar
endptTFTPDIR=_EndptTFTPDIR_Object((1,3,6,1,4,1,6889,2,69,1,1,18),_EndptTFTPDIR_Type())
endptTFTPDIR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptTFTPDIR.setStatus(_B)
_EndptTFTPSRVR_Type=DisplayString
_EndptTFTPSRVR_Object=MibScalar
endptTFTPSRVR=_EndptTFTPSRVR_Object((1,3,6,1,4,1,6889,2,69,1,1,19),_EndptTFTPSRVR_Type())
endptTFTPSRVR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptTFTPSRVR.setStatus(_B)
_EndptTFTPINUSE_Type=IpAddress
_EndptTFTPINUSE_Object=MibScalar
endptTFTPINUSE=_EndptTFTPINUSE_Object((1,3,6,1,4,1,6889,2,69,1,1,20),_EndptTFTPINUSE_Type())
endptTFTPINUSE.setMaxAccess(_A)
if mibBuilder.loadTexts:endptTFTPINUSE.setStatus(_B)
_EndptBOOTNAME_Type=DisplayString
_EndptBOOTNAME_Object=MibScalar
endptBOOTNAME=_EndptBOOTNAME_Object((1,3,6,1,4,1,6889,2,69,1,1,21),_EndptBOOTNAME_Type())
endptBOOTNAME.setMaxAccess(_A)
if mibBuilder.loadTexts:endptBOOTNAME.setStatus(_B)
_EndptAPPNAME_Type=DisplayString
_EndptAPPNAME_Object=MibScalar
endptAPPNAME=_EndptAPPNAME_Object((1,3,6,1,4,1,6889,2,69,1,1,22),_EndptAPPNAME_Type())
endptAPPNAME.setMaxAccess(_A)
if mibBuilder.loadTexts:endptAPPNAME.setStatus(_B)
_EndptSSON_Type=Integer32
_EndptSSON_Object=MibScalar
endptSSON=_EndptSSON_Object((1,3,6,1,4,1,6889,2,69,1,1,23),_EndptSSON_Type())
endptSSON.setMaxAccess(_A)
if mibBuilder.loadTexts:endptSSON.setStatus(_C)
_EndptBBURST_Type=Integer32
_EndptBBURST_Object=MibScalar
endptBBURST=_EndptBBURST_Object((1,3,6,1,4,1,6889,2,69,1,1,24),_EndptBBURST_Type())
endptBBURST.setMaxAccess(_A)
if mibBuilder.loadTexts:endptBBURST.setStatus(_C)
_EndptHUBSTAT_Type=Integer32
_EndptHUBSTAT_Object=MibScalar
endptHUBSTAT=_EndptHUBSTAT_Object((1,3,6,1,4,1,6889,2,69,1,1,25),_EndptHUBSTAT_Type())
endptHUBSTAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptHUBSTAT.setStatus(_C)
_EndptDSCPAUD_Type=Integer32
_EndptDSCPAUD_Object=MibScalar
endptDSCPAUD=_EndptDSCPAUD_Object((1,3,6,1,4,1,6889,2,69,1,1,26),_EndptDSCPAUD_Type())
endptDSCPAUD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDSCPAUD.setStatus(_B)
_EndptDSCPSIG_Type=Integer32
_EndptDSCPSIG_Object=MibScalar
endptDSCPSIG=_EndptDSCPSIG_Object((1,3,6,1,4,1,6889,2,69,1,1,27),_EndptDSCPSIG_Type())
endptDSCPSIG.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDSCPSIG.setStatus(_B)
_EndptL2Q_Type=Integer32
_EndptL2Q_Object=MibScalar
endptL2Q=_EndptL2Q_Object((1,3,6,1,4,1,6889,2,69,1,1,28),_EndptL2Q_Type())
endptL2Q.setMaxAccess(_A)
if mibBuilder.loadTexts:endptL2Q.setStatus(_B)
_EndptL2QAUD_Type=Integer32
_EndptL2QAUD_Object=MibScalar
endptL2QAUD=_EndptL2QAUD_Object((1,3,6,1,4,1,6889,2,69,1,1,29),_EndptL2QAUD_Type())
endptL2QAUD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptL2QAUD.setStatus(_B)
_EndptL2QSIG_Type=Integer32
_EndptL2QSIG_Object=MibScalar
endptL2QSIG=_EndptL2QSIG_Object((1,3,6,1,4,1,6889,2,69,1,1,30),_EndptL2QSIG_Type())
endptL2QSIG.setMaxAccess(_A)
if mibBuilder.loadTexts:endptL2QSIG.setStatus(_B)
_EndptL2QVLAN_Type=Integer32
_EndptL2QVLAN_Object=MibScalar
endptL2QVLAN=_EndptL2QVLAN_Object((1,3,6,1,4,1,6889,2,69,1,1,31),_EndptL2QVLAN_Type())
endptL2QVLAN.setMaxAccess(_A)
if mibBuilder.loadTexts:endptL2QVLAN.setStatus(_B)
_Endpt46XXUPGR_Type=DisplayString
_Endpt46XXUPGR_Object=MibScalar
endpt46XXUPGR=_Endpt46XXUPGR_Object((1,3,6,1,4,1,6889,2,69,1,1,32),_Endpt46XXUPGR_Type())
endpt46XXUPGR.setMaxAccess(_A)
if mibBuilder.loadTexts:endpt46XXUPGR.setStatus(_B)
_EndptDNSSRVR_Type=DisplayString
_EndptDNSSRVR_Object=MibScalar
endptDNSSRVR=_EndptDNSSRVR_Object((1,3,6,1,4,1,6889,2,69,1,1,33),_EndptDNSSRVR_Type())
endptDNSSRVR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDNSSRVR.setStatus(_B)
_EndptDNSINUSE_Type=IpAddress
_EndptDNSINUSE_Object=MibScalar
endptDNSINUSE=_EndptDNSINUSE_Object((1,3,6,1,4,1,6889,2,69,1,1,34),_EndptDNSINUSE_Type())
endptDNSINUSE.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDNSINUSE.setStatus(_C)
_EndptDOMAIN_Type=DisplayString
_EndptDOMAIN_Object=MibScalar
endptDOMAIN=_EndptDOMAIN_Object((1,3,6,1,4,1,6889,2,69,1,1,35),_EndptDOMAIN_Type())
endptDOMAIN.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDOMAIN.setStatus(_B)
_EndptRTCPMON_Type=IpAddress
_EndptRTCPMON_Object=MibScalar
endptRTCPMON=_EndptRTCPMON_Object((1,3,6,1,4,1,6889,2,69,1,1,36),_EndptRTCPMON_Type())
endptRTCPMON.setMaxAccess(_A)
if mibBuilder.loadTexts:endptRTCPMON.setStatus(_B)
_EndptPHY2STAT_Type=Integer32
_EndptPHY2STAT_Object=MibScalar
endptPHY2STAT=_EndptPHY2STAT_Object((1,3,6,1,4,1,6889,2,69,1,1,37),_EndptPHY2STAT_Type())
endptPHY2STAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPHY2STAT.setStatus(_B)
_EndptIRSTAT_Type=Integer32
_EndptIRSTAT_Object=MibScalar
endptIRSTAT=_EndptIRSTAT_Object((1,3,6,1,4,1,6889,2,69,1,1,38),_EndptIRSTAT_Type())
endptIRSTAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptIRSTAT.setStatus(_B)
_EndptSMTPSRVR_Type=DisplayString
_EndptSMTPSRVR_Object=MibScalar
endptSMTPSRVR=_EndptSMTPSRVR_Object((1,3,6,1,4,1,6889,2,69,1,1,39),_EndptSMTPSRVR_Type())
endptSMTPSRVR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptSMTPSRVR.setStatus(_B)
_EndptDSPVERSION_Type=DisplayString
_EndptDSPVERSION_Object=MibScalar
endptDSPVERSION=_EndptDSPVERSION_Object((1,3,6,1,4,1,6889,2,69,1,1,40),_EndptDSPVERSION_Type())
endptDSPVERSION.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDSPVERSION.setStatus(_B)
_EndptLOGSRVR_Type=DisplayString
_EndptLOGSRVR_Object=MibScalar
endptLOGSRVR=_EndptLOGSRVR_Object((1,3,6,1,4,1,6889,2,69,1,1,41),_EndptLOGSRVR_Type())
endptLOGSRVR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptLOGSRVR.setStatus(_B)
_EndptLOGSTAT_Type=Integer32
_EndptLOGSTAT_Object=MibScalar
endptLOGSTAT=_EndptLOGSTAT_Object((1,3,6,1,4,1,6889,2,69,1,1,42),_EndptLOGSTAT_Type())
endptLOGSTAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptLOGSTAT.setStatus(_C)
_EndptAGCHAND_Type=Integer32
_EndptAGCHAND_Object=MibScalar
endptAGCHAND=_EndptAGCHAND_Object((1,3,6,1,4,1,6889,2,69,1,1,43),_EndptAGCHAND_Type())
endptAGCHAND.setMaxAccess(_A)
if mibBuilder.loadTexts:endptAGCHAND.setStatus(_B)
_EndptAGCHEAD_Type=Integer32
_EndptAGCHEAD_Object=MibScalar
endptAGCHEAD=_EndptAGCHEAD_Object((1,3,6,1,4,1,6889,2,69,1,1,44),_EndptAGCHEAD_Type())
endptAGCHEAD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptAGCHEAD.setStatus(_B)
_EndptPHY1STAT_Type=Integer32
_EndptPHY1STAT_Object=MibScalar
endptPHY1STAT=_EndptPHY1STAT_Object((1,3,6,1,4,1,6889,2,69,1,1,45),_EndptPHY1STAT_Type())
endptPHY1STAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPHY1STAT.setStatus(_B)
_EndptL2QSTAT_Type=Integer32
_EndptL2QSTAT_Object=MibScalar
endptL2QSTAT=_EndptL2QSTAT_Object((1,3,6,1,4,1,6889,2,69,1,1,46),_EndptL2QSTAT_Type())
endptL2QSTAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptL2QSTAT.setStatus(_B)
_EndptVLANTEST_Type=Integer32
_EndptVLANTEST_Object=MibScalar
endptVLANTEST=_EndptVLANTEST_Object((1,3,6,1,4,1,6889,2,69,1,1,47),_EndptVLANTEST_Type())
endptVLANTEST.setMaxAccess(_A)
if mibBuilder.loadTexts:endptVLANTEST.setStatus(_C)
_EndptPHONECC_Type=DisplayString
_EndptPHONECC_Object=MibScalar
endptPHONECC=_EndptPHONECC_Object((1,3,6,1,4,1,6889,2,69,1,1,48),_EndptPHONECC_Type())
endptPHONECC.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPHONECC.setStatus(_B)
_EndptVLANLIST_Type=DisplayString
_EndptVLANLIST_Object=MibScalar
endptVLANLIST=_EndptVLANLIST_Object((1,3,6,1,4,1,6889,2,69,1,1,49),_EndptVLANLIST_Type())
endptVLANLIST.setMaxAccess(_A)
if mibBuilder.loadTexts:endptVLANLIST.setStatus(_B)
_EndptAGCSPKR_Type=Integer32
_EndptAGCSPKR_Object=MibScalar
endptAGCSPKR=_EndptAGCSPKR_Object((1,3,6,1,4,1,6889,2,69,1,1,50),_EndptAGCSPKR_Type())
endptAGCSPKR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptAGCSPKR.setStatus(_B)
_EndptHTTPSRVR_Type=DisplayString
_EndptHTTPSRVR_Object=MibScalar
endptHTTPSRVR=_EndptHTTPSRVR_Object((1,3,6,1,4,1,6889,2,69,1,1,51),_EndptHTTPSRVR_Type())
endptHTTPSRVR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptHTTPSRVR.setStatus(_B)
_EndptHTTPDIR_Type=DisplayString
_EndptHTTPDIR_Object=MibScalar
endptHTTPDIR=_EndptHTTPDIR_Object((1,3,6,1,4,1,6889,2,69,1,1,52),_EndptHTTPDIR_Type())
endptHTTPDIR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptHTTPDIR.setStatus(_B)
_EndptHTTPPORT_Type=Integer32
_EndptHTTPPORT_Object=MibScalar
endptHTTPPORT=_EndptHTTPPORT_Object((1,3,6,1,4,1,6889,2,69,1,1,53),_EndptHTTPPORT_Type())
endptHTTPPORT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptHTTPPORT.setStatus(_B)
_EndptHTTPUSED_Type=OctetString
_EndptHTTPUSED_Object=MibScalar
endptHTTPUSED=_EndptHTTPUSED_Object((1,3,6,1,4,1,6889,2,69,1,1,54),_EndptHTTPUSED_Type())
endptHTTPUSED.setMaxAccess(_A)
if mibBuilder.loadTexts:endptHTTPUSED.setStatus(_B)
_EndptPROCSTAT_Type=Integer32
_EndptPROCSTAT_Object=MibScalar
endptPROCSTAT=_EndptPROCSTAT_Object((1,3,6,1,4,1,6889,2,69,1,1,55),_EndptPROCSTAT_Type())
endptPROCSTAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPROCSTAT.setStatus(_B)
_EndptPROCPSWD_Type=Integer32
_EndptPROCPSWD_Object=MibScalar
endptPROCPSWD=_EndptPROCPSWD_Object((1,3,6,1,4,1,6889,2,69,1,1,56),_EndptPROCPSWD_Type())
endptPROCPSWD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPROCPSWD.setStatus(_B)
_EndptSIG_Type=Integer32
_EndptSIG_Object=MibScalar
endptSIG=_EndptSIG_Object((1,3,6,1,4,1,6889,2,69,1,1,57),_EndptSIG_Type())
endptSIG.setMaxAccess(_A)
if mibBuilder.loadTexts:endptSIG.setStatus(_B)
_EndptGROUP_Type=Integer32
_EndptGROUP_Object=MibScalar
endptGROUP=_EndptGROUP_Object((1,3,6,1,4,1,6889,2,69,1,1,58),_EndptGROUP_Type())
endptGROUP.setMaxAccess(_A)
if mibBuilder.loadTexts:endptGROUP.setStatus(_B)
_EndptSNMPADD_Type=DisplayString
_EndptSNMPADD_Object=MibScalar
endptSNMPADD=_EndptSNMPADD_Object((1,3,6,1,4,1,6889,2,69,1,1,59),_EndptSNMPADD_Type())
endptSNMPADD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptSNMPADD.setStatus(_B)
_EndptCODESRVR_Type=DisplayString
_EndptCODESRVR_Object=MibScalar
endptCODESRVR=_EndptCODESRVR_Object((1,3,6,1,4,1,6889,2,69,1,1,60),_EndptCODESRVR_Type())
endptCODESRVR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptCODESRVR.setStatus(_C)
_EndptCODEUSED_Type=OctetString
_EndptCODEUSED_Object=MibScalar
endptCODEUSED=_EndptCODEUSED_Object((1,3,6,1,4,1,6889,2,69,1,1,61),_EndptCODEUSED_Type())
endptCODEUSED.setMaxAccess(_A)
if mibBuilder.loadTexts:endptCODEUSED.setStatus(_C)
_EndptSTATIC_Type=Integer32
_EndptSTATIC_Object=MibScalar
endptSTATIC=_EndptSTATIC_Object((1,3,6,1,4,1,6889,2,69,1,1,62),_EndptSTATIC_Type())
endptSTATIC.setMaxAccess(_A)
if mibBuilder.loadTexts:endptSTATIC.setStatus(_B)
_EndptTLSSRVR_Type=DisplayString
_EndptTLSSRVR_Object=MibScalar
endptTLSSRVR=_EndptTLSSRVR_Object((1,3,6,1,4,1,6889,2,69,1,1,63),_EndptTLSSRVR_Type())
endptTLSSRVR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptTLSSRVR.setStatus(_B)
_EndptTLSUSED_Type=OctetString
_EndptTLSUSED_Object=MibScalar
endptTLSUSED=_EndptTLSUSED_Object((1,3,6,1,4,1,6889,2,69,1,1,64),_EndptTLSUSED_Type())
endptTLSUSED.setMaxAccess(_A)
if mibBuilder.loadTexts:endptTLSUSED.setStatus(_B)
_EndptCNAPORT_Type=Integer32
_EndptCNAPORT_Object=MibScalar
endptCNAPORT=_EndptCNAPORT_Object((1,3,6,1,4,1,6889,2,69,1,1,65),_EndptCNAPORT_Type())
endptCNAPORT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptCNAPORT.setStatus(_B)
_EndptCNASRVR_Type=DisplayString
_EndptCNASRVR_Object=MibScalar
endptCNASRVR=_EndptCNASRVR_Object((1,3,6,1,4,1,6889,2,69,1,1,66),_EndptCNASRVR_Type())
endptCNASRVR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptCNASRVR.setStatus(_B)
_EndptDSTOFFSET_Type=DisplayString
_EndptDSTOFFSET_Object=MibScalar
endptDSTOFFSET=_EndptDSTOFFSET_Object((1,3,6,1,4,1,6889,2,69,1,1,67),_EndptDSTOFFSET_Type())
endptDSTOFFSET.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDSTOFFSET.setStatus(_B)
_EndptDSTSTART_Type=DisplayString
_EndptDSTSTART_Object=MibScalar
endptDSTSTART=_EndptDSTSTART_Object((1,3,6,1,4,1,6889,2,69,1,1,68),_EndptDSTSTART_Type())
endptDSTSTART.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDSTSTART.setStatus(_B)
_EndptDSTSTOP_Type=DisplayString
_EndptDSTSTOP_Object=MibScalar
endptDSTSTOP=_EndptDSTSTOP_Object((1,3,6,1,4,1,6889,2,69,1,1,69),_EndptDSTSTOP_Type())
endptDSTSTOP.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDSTSTOP.setStatus(_B)
_EndptGMTOFFSET_Type=DisplayString
_EndptGMTOFFSET_Object=MibScalar
endptGMTOFFSET=_EndptGMTOFFSET_Object((1,3,6,1,4,1,6889,2,69,1,1,70),_EndptGMTOFFSET_Type())
endptGMTOFFSET.setMaxAccess(_A)
if mibBuilder.loadTexts:endptGMTOFFSET.setStatus(_B)
_EndptSNTPSRVR_Type=DisplayString
_EndptSNTPSRVR_Object=MibScalar
endptSNTPSRVR=_EndptSNTPSRVR_Object((1,3,6,1,4,1,6889,2,69,1,1,71),_EndptSNTPSRVR_Type())
endptSNTPSRVR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptSNTPSRVR.setStatus(_B)
_EndptBAKLIGHTOFF_Type=Integer32
_EndptBAKLIGHTOFF_Object=MibScalar
endptBAKLIGHTOFF=_EndptBAKLIGHTOFF_Object((1,3,6,1,4,1,6889,2,69,1,1,72),_EndptBAKLIGHTOFF_Type())
endptBAKLIGHTOFF.setMaxAccess(_A)
if mibBuilder.loadTexts:endptBAKLIGHTOFF.setStatus(_B)
_EndptDOT1X_Type=Integer32
_EndptDOT1X_Object=MibScalar
endptDOT1X=_EndptDOT1X_Object((1,3,6,1,4,1,6889,2,69,1,1,73),_EndptDOT1X_Type())
endptDOT1X.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDOT1X.setStatus(_B)
_EndptAUDIOENV_Type=Integer32
_EndptAUDIOENV_Object=MibScalar
endptAUDIOENV=_EndptAUDIOENV_Object((1,3,6,1,4,1,6889,2,69,1,1,74),_EndptAUDIOENV_Type())
endptAUDIOENV.setMaxAccess(_A)
if mibBuilder.loadTexts:endptAUDIOENV.setStatus(_B)
_EndptAUDIOSTHD_Type=Integer32
_EndptAUDIOSTHD_Object=MibScalar
endptAUDIOSTHD=_EndptAUDIOSTHD_Object((1,3,6,1,4,1,6889,2,69,1,1,75),_EndptAUDIOSTHD_Type())
endptAUDIOSTHD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptAUDIOSTHD.setStatus(_B)
_EndptAUDIOSTHS_Type=Integer32
_EndptAUDIOSTHS_Object=MibScalar
endptAUDIOSTHS=_EndptAUDIOSTHS_Object((1,3,6,1,4,1,6889,2,69,1,1,76),_EndptAUDIOSTHS_Type())
endptAUDIOSTHS.setMaxAccess(_A)
if mibBuilder.loadTexts:endptAUDIOSTHS.setStatus(_B)
_EndptDHCPINUSE_Type=IpAddress
_EndptDHCPINUSE_Object=MibScalar
endptDHCPINUSE=_EndptDHCPINUSE_Object((1,3,6,1,4,1,6889,2,69,1,1,77),_EndptDHCPINUSE_Type())
endptDHCPINUSE.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDHCPINUSE.setStatus(_B)
_EndptDHCPLEASEEXP_Type=Integer32
_EndptDHCPLEASEEXP_Object=MibScalar
endptDHCPLEASEEXP=_EndptDHCPLEASEEXP_Object((1,3,6,1,4,1,6889,2,69,1,1,78),_EndptDHCPLEASEEXP_Type())
endptDHCPLEASEEXP.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDHCPLEASEEXP.setStatus(_B)
_EndptDHCPSTD_Type=Integer32
_EndptDHCPSTD_Object=MibScalar
endptDHCPSTD=_EndptDHCPSTD_Object((1,3,6,1,4,1,6889,2,69,1,1,79),_EndptDHCPSTD_Type())
endptDHCPSTD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDHCPSTD.setStatus(_B)
_EndptDHCPT1REM_Type=Integer32
_EndptDHCPT1REM_Object=MibScalar
endptDHCPT1REM=_EndptDHCPT1REM_Object((1,3,6,1,4,1,6889,2,69,1,1,80),_EndptDHCPT1REM_Type())
endptDHCPT1REM.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDHCPT1REM.setStatus(_B)
_EndptDHCPT2REM_Type=Integer32
_EndptDHCPT2REM_Object=MibScalar
endptDHCPT2REM=_EndptDHCPT2REM_Object((1,3,6,1,4,1,6889,2,69,1,1,81),_EndptDHCPT2REM_Type())
endptDHCPT2REM.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDHCPT2REM.setStatus(_B)
_EndptICMPDU_Type=Integer32
_EndptICMPDU_Object=MibScalar
endptICMPDU=_EndptICMPDU_Object((1,3,6,1,4,1,6889,2,69,1,1,81),_EndptICMPDU_Type())
endptICMPDU.setMaxAccess(_A)
if mibBuilder.loadTexts:endptICMPDU.setStatus(_B)
_EndptICMPRED_Type=Integer32
_EndptICMPRED_Object=MibScalar
endptICMPRED=_EndptICMPRED_Object((1,3,6,1,4,1,6889,2,69,1,1,82),_EndptICMPRED_Type())
endptICMPRED.setMaxAccess(_A)
if mibBuilder.loadTexts:endptICMPRED.setStatus(_B)
_EndptSSONCONTENT_Type=DisplayString
_EndptSSONCONTENT_Object=MibScalar
endptSSONCONTENT=_EndptSSONCONTENT_Object((1,3,6,1,4,1,6889,2,69,1,1,83),_EndptSSONCONTENT_Type())
endptSSONCONTENT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptSSONCONTENT.setStatus(_B)
_EndptBRURI_Type=DisplayString
_EndptBRURI_Object=MibScalar
endptBRURI=_EndptBRURI_Object((1,3,6,1,4,1,6889,2,69,1,1,84),_EndptBRURI_Type())
endptBRURI.setMaxAccess(_A)
if mibBuilder.loadTexts:endptBRURI.setStatus(_B)
_EndptNVM_ObjectIdentity=ObjectIdentity
endptNVM=_EndptNVM_ObjectIdentity((1,3,6,1,4,1,6889,2,69,1,2))
_EndptNVMCIPADD_Type=DisplayString
_EndptNVMCIPADD_Object=MibScalar
endptNVMCIPADD=_EndptNVMCIPADD_Object((1,3,6,1,4,1,6889,2,69,1,2,1),_EndptNVMCIPADD_Type())
endptNVMCIPADD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVMCIPADD.setStatus(_B)
_EndptNVMCPORT_Type=Integer32
_EndptNVMCPORT_Object=MibScalar
endptNVMCPORT=_EndptNVMCPORT_Object((1,3,6,1,4,1,6889,2,69,1,2,2),_EndptNVMCPORT_Type())
endptNVMCPORT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVMCPORT.setStatus(_C)
_EndptNVIPADD_Type=DisplayString
_EndptNVIPADD_Object=MibScalar
endptNVIPADD=_EndptNVIPADD_Object((1,3,6,1,4,1,6889,2,69,1,2,3),_EndptNVIPADD_Type())
endptNVIPADD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVIPADD.setStatus(_B)
_EndptNVGIPADD_Type=DisplayString
_EndptNVGIPADD_Object=MibScalar
endptNVGIPADD=_EndptNVGIPADD_Object((1,3,6,1,4,1,6889,2,69,1,2,4),_EndptNVGIPADD_Type())
endptNVGIPADD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVGIPADD.setStatus(_B)
_EndptNVNETMASK_Type=DisplayString
_EndptNVNETMASK_Object=MibScalar
endptNVNETMASK=_EndptNVNETMASK_Object((1,3,6,1,4,1,6889,2,69,1,2,5),_EndptNVNETMASK_Type())
endptNVNETMASK.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVNETMASK.setStatus(_B)
_EndptNVTFTPSRVR_Type=DisplayString
_EndptNVTFTPSRVR_Object=MibScalar
endptNVTFTPSRVR=_EndptNVTFTPSRVR_Object((1,3,6,1,4,1,6889,2,69,1,2,6),_EndptNVTFTPSRVR_Type())
endptNVTFTPSRVR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVTFTPSRVR.setStatus(_C)
_EndptNVSSON_Type=Integer32
_EndptNVSSON_Object=MibScalar
endptNVSSON=_EndptNVSSON_Object((1,3,6,1,4,1,6889,2,69,1,2,7),_EndptNVSSON_Type())
endptNVSSON.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVSSON.setStatus(_B)
_EndptNVBBURST_Type=Integer32
_EndptNVBBURST_Object=MibScalar
endptNVBBURST=_EndptNVBBURST_Object((1,3,6,1,4,1,6889,2,69,1,2,8),_EndptNVBBURST_Type())
endptNVBBURST.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVBBURST.setStatus(_C)
_EndptNVHUBSTAT_Type=Integer32
_EndptNVHUBSTAT_Object=MibScalar
endptNVHUBSTAT=_EndptNVHUBSTAT_Object((1,3,6,1,4,1,6889,2,69,1,2,9),_EndptNVHUBSTAT_Type())
endptNVHUBSTAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVHUBSTAT.setStatus(_C)
_EndptNVDSCPAUD_Type=Integer32
_EndptNVDSCPAUD_Object=MibScalar
endptNVDSCPAUD=_EndptNVDSCPAUD_Object((1,3,6,1,4,1,6889,2,69,1,2,10),_EndptNVDSCPAUD_Type())
endptNVDSCPAUD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVDSCPAUD.setStatus(_B)
_EndptNVDSCPSIG_Type=Integer32
_EndptNVDSCPSIG_Object=MibScalar
endptNVDSCPSIG=_EndptNVDSCPSIG_Object((1,3,6,1,4,1,6889,2,69,1,2,11),_EndptNVDSCPSIG_Type())
endptNVDSCPSIG.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVDSCPSIG.setStatus(_B)
_EndptNVL2Q_Type=Integer32
_EndptNVL2Q_Object=MibScalar
endptNVL2Q=_EndptNVL2Q_Object((1,3,6,1,4,1,6889,2,69,1,2,12),_EndptNVL2Q_Type())
endptNVL2Q.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVL2Q.setStatus(_B)
_EndptNVL2QAUD_Type=Integer32
_EndptNVL2QAUD_Object=MibScalar
endptNVL2QAUD=_EndptNVL2QAUD_Object((1,3,6,1,4,1,6889,2,69,1,2,13),_EndptNVL2QAUD_Type())
endptNVL2QAUD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVL2QAUD.setStatus(_B)
_EndptNVL2QSIG_Type=Integer32
_EndptNVL2QSIG_Object=MibScalar
endptNVL2QSIG=_EndptNVL2QSIG_Object((1,3,6,1,4,1,6889,2,69,1,2,14),_EndptNVL2QSIG_Type())
endptNVL2QSIG.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVL2QSIG.setStatus(_B)
_EndptNVL2QVLAN_Type=Integer32
_EndptNVL2QVLAN_Object=MibScalar
endptNVL2QVLAN=_EndptNVL2QVLAN_Object((1,3,6,1,4,1,6889,2,69,1,2,15),_EndptNVL2QVLAN_Type())
endptNVL2QVLAN.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVL2QVLAN.setStatus(_B)
_EndptNVPHY2STAT_Type=Integer32
_EndptNVPHY2STAT_Object=MibScalar
endptNVPHY2STAT=_EndptNVPHY2STAT_Object((1,3,6,1,4,1,6889,2,69,1,2,16),_EndptNVPHY2STAT_Type())
endptNVPHY2STAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVPHY2STAT.setStatus(_B)
_EndptNVLOGSTAT_Type=Integer32
_EndptNVLOGSTAT_Object=MibScalar
endptNVLOGSTAT=_EndptNVLOGSTAT_Object((1,3,6,1,4,1,6889,2,69,1,2,17),_EndptNVLOGSTAT_Type())
endptNVLOGSTAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVLOGSTAT.setStatus(_B)
_EndptNVAGCHAND_Type=Integer32
_EndptNVAGCHAND_Object=MibScalar
endptNVAGCHAND=_EndptNVAGCHAND_Object((1,3,6,1,4,1,6889,2,69,1,2,18),_EndptNVAGCHAND_Type())
endptNVAGCHAND.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVAGCHAND.setStatus(_B)
_EndptNVAGCHEAD_Type=Integer32
_EndptNVAGCHEAD_Object=MibScalar
endptNVAGCHEAD=_EndptNVAGCHEAD_Object((1,3,6,1,4,1,6889,2,69,1,2,19),_EndptNVAGCHEAD_Type())
endptNVAGCHEAD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVAGCHEAD.setStatus(_B)
_EndptNVIRSTAT_Type=Integer32
_EndptNVIRSTAT_Object=MibScalar
endptNVIRSTAT=_EndptNVIRSTAT_Object((1,3,6,1,4,1,6889,2,69,1,2,20),_EndptNVIRSTAT_Type())
endptNVIRSTAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVIRSTAT.setStatus(_B)
_EndptNVPHY1STAT_Type=Integer32
_EndptNVPHY1STAT_Object=MibScalar
endptNVPHY1STAT=_EndptNVPHY1STAT_Object((1,3,6,1,4,1,6889,2,69,1,2,21),_EndptNVPHY1STAT_Type())
endptNVPHY1STAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVPHY1STAT.setStatus(_B)
_EndptNVVLANTEST_Type=Integer32
_EndptNVVLANTEST_Object=MibScalar
endptNVVLANTEST=_EndptNVVLANTEST_Object((1,3,6,1,4,1,6889,2,69,1,2,22),_EndptNVVLANTEST_Type())
endptNVVLANTEST.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVVLANTEST.setStatus(_B)
_EndptNVVLANLIST_Type=DisplayString
_EndptNVVLANLIST_Object=MibScalar
endptNVVLANLIST=_EndptNVVLANLIST_Object((1,3,6,1,4,1,6889,2,69,1,2,23),_EndptNVVLANLIST_Type())
endptNVVLANLIST.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVVLANLIST.setStatus(_C)
_EndptNVAGCSPKR_Type=Integer32
_EndptNVAGCSPKR_Object=MibScalar
endptNVAGCSPKR=_EndptNVAGCSPKR_Object((1,3,6,1,4,1,6889,2,69,1,2,24),_EndptNVAGCSPKR_Type())
endptNVAGCSPKR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVAGCSPKR.setStatus(_B)
_EndptNVHTTPSRVR_Type=DisplayString
_EndptNVHTTPSRVR_Object=MibScalar
endptNVHTTPSRVR=_EndptNVHTTPSRVR_Object((1,3,6,1,4,1,6889,2,69,1,2,25),_EndptNVHTTPSRVR_Type())
endptNVHTTPSRVR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVHTTPSRVR.setStatus(_C)
_EndptNVAUTH_Type=Integer32
_EndptNVAUTH_Object=MibScalar
endptNVAUTH=_EndptNVAUTH_Object((1,3,6,1,4,1,6889,2,69,1,2,26),_EndptNVAUTH_Type())
endptNVAUTH.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVAUTH.setStatus(_B)
_EndptNVFILESRVR_Type=DisplayString
_EndptNVFILESRVR_Object=MibScalar
endptNVFILESRVR=_EndptNVFILESRVR_Object((1,3,6,1,4,1,6889,2,69,1,2,27),_EndptNVFILESRVR_Type())
endptNVFILESRVR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVFILESRVR.setStatus(_B)
_EndptNVALERT_Type=Integer32
_EndptNVALERT_Object=MibScalar
endptNVALERT=_EndptNVALERT_Object((1,3,6,1,4,1,6889,2,69,1,2,28),_EndptNVALERT_Type())
endptNVALERT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVALERT.setStatus(_B)
_EndptNVCHADDR_Type=Integer32
_EndptNVCHADDR_Object=MibScalar
endptNVCHADDR=_EndptNVCHADDR_Object((1,3,6,1,4,1,6889,2,69,1,2,29),_EndptNVCHADDR_Type())
endptNVCHADDR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVCHADDR.setStatus(_B)
_EndptNVCONTRAST_Type=Integer32
_EndptNVCONTRAST_Object=MibScalar
endptNVCONTRAST=_EndptNVCONTRAST_Object((1,3,6,1,4,1,6889,2,69,1,2,30),_EndptNVCONTRAST_Type())
endptNVCONTRAST.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVCONTRAST.setStatus(_B)
_EndptMaintenance_ObjectIdentity=ObjectIdentity
endptMaintenance=_EndptMaintenance_ObjectIdentity((1,3,6,1,4,1,6889,2,69,1,3))
_EndptUPGRADESCRIPT_Type=Integer32
_EndptUPGRADESCRIPT_Object=MibScalar
endptUPGRADESCRIPT=_EndptUPGRADESCRIPT_Object((1,3,6,1,4,1,6889,2,69,1,3,1),_EndptUPGRADESCRIPT_Type())
endptUPGRADESCRIPT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptUPGRADESCRIPT.setStatus(_B)
_EndptAPPINUSE_Type=DisplayString
_EndptAPPINUSE_Object=MibScalar
endptAPPINUSE=_EndptAPPINUSE_Object((1,3,6,1,4,1,6889,2,69,1,3,2),_EndptAPPINUSE_Type())
endptAPPINUSE.setMaxAccess(_A)
if mibBuilder.loadTexts:endptAPPINUSE.setStatus(_B)
_EndptAPPSTAT_Type=Integer32
_EndptAPPSTAT_Object=MibScalar
endptAPPSTAT=_EndptAPPSTAT_Object((1,3,6,1,4,1,6889,2,69,1,3,3),_EndptAPPSTAT_Type())
endptAPPSTAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptAPPSTAT.setStatus(_B)
_EndptRecentLog_Object=MibTable
endptRecentLog=_EndptRecentLog_Object((1,3,6,1,4,1,6889,2,69,1,3,4))
if mibBuilder.loadTexts:endptRecentLog.setStatus(_B)
_EndptRecentLogEntry_Object=MibTableRow
endptRecentLogEntry=_EndptRecentLogEntry_Object((1,3,6,1,4,1,6889,2,69,1,3,4,1))
endptRecentLogEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:endptRecentLogEntry.setStatus(_B)
_EndptRecentLogText_Type=DisplayString
_EndptRecentLogText_Object=MibTableColumn
endptRecentLogText=_EndptRecentLogText_Object((1,3,6,1,4,1,6889,2,69,1,3,4,1,1),_EndptRecentLogText_Type())
endptRecentLogText.setMaxAccess(_A)
if mibBuilder.loadTexts:endptRecentLogText.setStatus(_B)
_EndptResetLog_Object=MibTable
endptResetLog=_EndptResetLog_Object((1,3,6,1,4,1,6889,2,69,1,3,5))
if mibBuilder.loadTexts:endptResetLog.setStatus(_B)
_EndptResetLogEntry_Object=MibTableRow
endptResetLogEntry=_EndptResetLogEntry_Object((1,3,6,1,4,1,6889,2,69,1,3,5,1))
endptResetLogEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:endptResetLogEntry.setStatus(_B)
_EndptResetLogText_Type=DisplayString
_EndptResetLogText_Object=MibTableColumn
endptResetLogText=_EndptResetLogText_Object((1,3,6,1,4,1,6889,2,69,1,3,5,1,1),_EndptResetLogText_Type())
endptResetLogText.setMaxAccess(_A)
if mibBuilder.loadTexts:endptResetLogText.setStatus(_B)
_EndptDEFINITY_ObjectIdentity=ObjectIdentity
endptDEFINITY=_EndptDEFINITY_ObjectIdentity((1,3,6,1,4,1,6889,2,69,1,4))
_EndptPORTAUD_Type=Integer32
_EndptPORTAUD_Object=MibScalar
endptPORTAUD=_EndptPORTAUD_Object((1,3,6,1,4,1,6889,2,69,1,4,1),_EndptPORTAUD_Type())
endptPORTAUD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPORTAUD.setStatus(_B)
_EndptPORTSIG_Type=Integer32
_EndptPORTSIG_Object=MibScalar
endptPORTSIG=_EndptPORTSIG_Object((1,3,6,1,4,1,6889,2,69,1,4,2),_EndptPORTSIG_Type())
endptPORTSIG.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPORTSIG.setStatus(_B)
_EndptFEIPADD_Type=OctetString
_EndptFEIPADD_Object=MibScalar
endptFEIPADD=_EndptFEIPADD_Object((1,3,6,1,4,1,6889,2,69,1,4,3),_EndptFEIPADD_Type())
endptFEIPADD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptFEIPADD.setStatus(_B)
_EndptFEPORT_Type=Integer32
_EndptFEPORT_Object=MibScalar
endptFEPORT=_EndptFEPORT_Object((1,3,6,1,4,1,6889,2,69,1,4,4),_EndptFEPORT_Type())
endptFEPORT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptFEPORT.setStatus(_B)
_EndptCODECR_Type=DisplayString
_EndptCODECR_Object=MibScalar
endptCODECR=_EndptCODECR_Object((1,3,6,1,4,1,6889,2,69,1,4,5),_EndptCODECR_Type())
endptCODECR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptCODECR.setStatus(_B)
_EndptCODECT_Type=DisplayString
_EndptCODECT_Object=MibScalar
endptCODECT=_EndptCODECT_Object((1,3,6,1,4,1,6889,2,69,1,4,6),_EndptCODECT_Type())
endptCODECT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptCODECT.setStatus(_B)
_EndptJCPC_Type=Integer32
_EndptJCPC_Object=MibScalar
endptJCPC=_EndptJCPC_Object((1,3,6,1,4,1,6889,2,69,1,4,7),_EndptJCPC_Type())
endptJCPC.setMaxAccess(_A)
if mibBuilder.loadTexts:endptJCPC.setStatus(_B)
_EndptTMSEC_Type=Integer32
_EndptTMSEC_Object=MibScalar
endptTMSEC=_EndptTMSEC_Object((1,3,6,1,4,1,6889,2,69,1,4,8),_EndptTMSEC_Type())
endptTMSEC.setMaxAccess(_A)
if mibBuilder.loadTexts:endptTMSEC.setStatus(_B)
_EndptNVPHONEXT_Type=DisplayString
_EndptNVPHONEXT_Object=MibScalar
endptNVPHONEXT=_EndptNVPHONEXT_Object((1,3,6,1,4,1,6889,2,69,1,4,9),_EndptNVPHONEXT_Type())
endptNVPHONEXT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNVPHONEXT.setStatus(_B)
_EndptL2QBBE_Type=Integer32
_EndptL2QBBE_Object=MibScalar
endptL2QBBE=_EndptL2QBBE_Object((1,3,6,1,4,1,6889,2,69,1,4,10),_EndptL2QBBE_Type())
endptL2QBBE.setMaxAccess(_A)
if mibBuilder.loadTexts:endptL2QBBE.setStatus(_C)
_EndptDSCPBBE_Type=Integer32
_EndptDSCPBBE_Object=MibScalar
endptDSCPBBE=_EndptDSCPBBE_Object((1,3,6,1,4,1,6889,2,69,1,4,11),_EndptDSCPBBE_Type())
endptDSCPBBE.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDSCPBBE.setStatus(_B)
_EndptRTCPCONT_Type=Integer32
_EndptRTCPCONT_Object=MibScalar
endptRTCPCONT=_EndptRTCPCONT_Object((1,3,6,1,4,1,6889,2,69,1,4,12),_EndptRTCPCONT_Type())
endptRTCPCONT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptRTCPCONT.setStatus(_B)
_EndptRTCPFLOW_Type=Integer32
_EndptRTCPFLOW_Object=MibScalar
endptRTCPFLOW=_EndptRTCPFLOW_Object((1,3,6,1,4,1,6889,2,69,1,4,13),_EndptRTCPFLOW_Type())
endptRTCPFLOW.setMaxAccess(_A)
if mibBuilder.loadTexts:endptRTCPFLOW.setStatus(_B)
_EndptRSVPCONT_Type=Integer32
_EndptRSVPCONT_Object=MibScalar
endptRSVPCONT=_EndptRSVPCONT_Object((1,3,6,1,4,1,6889,2,69,1,4,14),_EndptRSVPCONT_Type())
endptRSVPCONT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptRSVPCONT.setStatus(_B)
_EndptRSVPRFRSH_Type=Integer32
_EndptRSVPRFRSH_Object=MibScalar
endptRSVPRFRSH=_EndptRSVPRFRSH_Object((1,3,6,1,4,1,6889,2,69,1,4,15),_EndptRSVPRFRSH_Type())
endptRSVPRFRSH.setMaxAccess(_A)
if mibBuilder.loadTexts:endptRSVPRFRSH.setStatus(_B)
_EndptRSVPRTRY_Type=Integer32
_EndptRSVPRTRY_Object=MibScalar
endptRSVPRTRY=_EndptRSVPRTRY_Object((1,3,6,1,4,1,6889,2,69,1,4,16),_EndptRSVPRTRY_Type())
endptRSVPRTRY.setMaxAccess(_A)
if mibBuilder.loadTexts:endptRSVPRTRY.setStatus(_B)
_EndptRSVPPROF_Type=Integer32
_EndptRSVPPROF_Object=MibScalar
endptRSVPPROF=_EndptRSVPPROF_Object((1,3,6,1,4,1,6889,2,69,1,4,17),_EndptRSVPPROF_Type())
endptRSVPPROF.setMaxAccess(_A)
if mibBuilder.loadTexts:endptRSVPPROF.setStatus(_B)
_EndptPHNCC_Type=Integer32
_EndptPHNCC_Object=MibScalar
endptPHNCC=_EndptPHNCC_Object((1,3,6,1,4,1,6889,2,69,1,4,18),_EndptPHNCC_Type())
endptPHNCC.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPHNCC.setStatus(_B)
_EndptPHNDPLENGTH_Type=Integer32
_EndptPHNDPLENGTH_Object=MibScalar
endptPHNDPLENGTH=_EndptPHNDPLENGTH_Object((1,3,6,1,4,1,6889,2,69,1,4,19),_EndptPHNDPLENGTH_Type())
endptPHNDPLENGTH.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPHNDPLENGTH.setStatus(_B)
_EndptPHNIC_Type=Integer32
_EndptPHNIC_Object=MibScalar
endptPHNIC=_EndptPHNIC_Object((1,3,6,1,4,1,6889,2,69,1,4,20),_EndptPHNIC_Type())
endptPHNIC.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPHNIC.setStatus(_B)
_EndptPHNLD_Type=Integer32
_EndptPHNLD_Object=MibScalar
endptPHNLD=_EndptPHNLD_Object((1,3,6,1,4,1,6889,2,69,1,4,21),_EndptPHNLD_Type())
endptPHNLD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPHNLD.setStatus(_B)
_EndptPHNLDLENGTH_Type=Integer32
_EndptPHNLDLENGTH_Object=MibScalar
endptPHNLDLENGTH=_EndptPHNLDLENGTH_Object((1,3,6,1,4,1,6889,2,69,1,4,22),_EndptPHNLDLENGTH_Type())
endptPHNLDLENGTH.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPHNLDLENGTH.setStatus(_B)
_EndptPHNOL_Type=Integer32
_EndptPHNOL_Object=MibScalar
endptPHNOL=_EndptPHNOL_Object((1,3,6,1,4,1,6889,2,69,1,4,23),_EndptPHNOL_Type())
endptPHNOL.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPHNOL.setStatus(_B)
_EndptNTWKAUDIO_Type=Integer32
_EndptNTWKAUDIO_Object=MibScalar
endptNTWKAUDIO=_EndptNTWKAUDIO_Object((1,3,6,1,4,1,6889,2,69,1,4,24),_EndptNTWKAUDIO_Type())
endptNTWKAUDIO.setMaxAccess(_A)
if mibBuilder.loadTexts:endptNTWKAUDIO.setStatus(_B)
_EndptENHDIALSTAT_Type=Integer32
_EndptENHDIALSTAT_Object=MibScalar
endptENHDIALSTAT=_EndptENHDIALSTAT_Object((1,3,6,1,4,1,6889,2,69,1,4,25),_EndptENHDIALSTAT_Type())
endptENHDIALSTAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptENHDIALSTAT.setStatus(_B)
_EndptRESTORESTAT_Type=Integer32
_EndptRESTORESTAT_Object=MibScalar
endptRESTORESTAT=_EndptRESTORESTAT_Object((1,3,6,1,4,1,6889,2,69,1,4,26),_EndptRESTORESTAT_Type())
endptRESTORESTAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptRESTORESTAT.setStatus(_B)
_EndptFTPUSERSTAT_Type=Integer32
_EndptFTPUSERSTAT_Object=MibScalar
endptFTPUSERSTAT=_EndptFTPUSERSTAT_Object((1,3,6,1,4,1,6889,2,69,1,4,27),_EndptFTPUSERSTAT_Type())
endptFTPUSERSTAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptFTPUSERSTAT.setStatus(_B)
_EndptRASGkList_Object=MibTable
endptRASGkList=_EndptRASGkList_Object((1,3,6,1,4,1,6889,2,69,1,4,28))
if mibBuilder.loadTexts:endptRASGkList.setStatus(_B)
_EndptRASGkEntry_Object=MibTableRow
endptRASGkEntry=_EndptRASGkEntry_Object((1,3,6,1,4,1,6889,2,69,1,4,28,1))
endptRASGkEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:endptRASGkEntry.setStatus(_B)
_EndptRASGkEntryData_Type=DisplayString
_EndptRASGkEntryData_Object=MibTableColumn
endptRASGkEntryData=_EndptRASGkEntryData_Object((1,3,6,1,4,1,6889,2,69,1,4,28,1,1),_EndptRASGkEntryData_Type())
endptRASGkEntryData.setMaxAccess(_A)
if mibBuilder.loadTexts:endptRASGkEntryData.setStatus(_B)
_EndptAdvApps_ObjectIdentity=ObjectIdentity
endptAdvApps=_EndptAdvApps_ObjectIdentity((1,3,6,1,4,1,6889,2,69,1,5))
_EndptCIBURL_Type=DisplayString
_EndptCIBURL_Object=MibScalar
endptCIBURL=_EndptCIBURL_Object((1,3,6,1,4,1,6889,2,69,1,5,1),_EndptCIBURL_Type())
endptCIBURL.setMaxAccess(_A)
if mibBuilder.loadTexts:endptCIBURL.setStatus(_C)
_EndptDIRSRVR_Type=OctetString
_EndptDIRSRVR_Object=MibScalar
endptDIRSRVR=_EndptDIRSRVR_Object((1,3,6,1,4,1,6889,2,69,1,5,2),_EndptDIRSRVR_Type())
endptDIRSRVR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDIRSRVR.setStatus(_B)
_EndptDIRTOPDN_Type=DisplayString
_EndptDIRTOPDN_Object=MibScalar
endptDIRTOPDN=_EndptDIRTOPDN_Object((1,3,6,1,4,1,6889,2,69,1,5,3),_EndptDIRTOPDN_Type())
endptDIRTOPDN.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDIRTOPDN.setStatus(_B)
_EndptDIRFULLNAME_Type=DisplayString
_EndptDIRFULLNAME_Object=MibScalar
endptDIRFULLNAME=_EndptDIRFULLNAME_Object((1,3,6,1,4,1,6889,2,69,1,5,4),_EndptDIRFULLNAME_Type())
endptDIRFULLNAME.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDIRFULLNAME.setStatus(_B)
_EndptDIRTELNUM_Type=DisplayString
_EndptDIRTELNUM_Object=MibScalar
endptDIRTELNUM=_EndptDIRTELNUM_Object((1,3,6,1,4,1,6889,2,69,1,5,5),_EndptDIRTELNUM_Type())
endptDIRTELNUM.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDIRTELNUM.setStatus(_B)
_EndptDIRSRCHTIME_Type=Integer32
_EndptDIRSRCHTIME_Object=MibScalar
endptDIRSRCHTIME=_EndptDIRSRCHTIME_Object((1,3,6,1,4,1,6889,2,69,1,5,6),_EndptDIRSRCHTIME_Type())
endptDIRSRCHTIME.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDIRSRCHTIME.setStatus(_B)
_EndptDIRSRVRPWD_Type=DisplayString
_EndptDIRSRVRPWD_Object=MibScalar
endptDIRSRVRPWD=_EndptDIRSRVRPWD_Object((1,3,6,1,4,1,6889,2,69,1,5,7),_EndptDIRSRVRPWD_Type())
endptDIRSRVRPWD.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDIRSRVRPWD.setStatus(_B)
_EndptDIRUSERID_Type=DisplayString
_EndptDIRUSERID_Object=MibScalar
endptDIRUSERID=_EndptDIRUSERID_Object((1,3,6,1,4,1,6889,2,69,1,5,8),_EndptDIRUSERID_Type())
endptDIRUSERID.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDIRUSERID.setStatus(_B)
_EndptDIRCODING_Type=DisplayString
_EndptDIRCODING_Object=MibScalar
endptDIRCODING=_EndptDIRCODING_Object((1,3,6,1,4,1,6889,2,69,1,5,9),_EndptDIRCODING_Type())
endptDIRCODING.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDIRCODING.setStatus(_B)
_EndptDIRSTAT_Type=Integer32
_EndptDIRSTAT_Object=MibScalar
endptDIRSTAT=_EndptDIRSTAT_Object((1,3,6,1,4,1,6889,2,69,1,5,10),_EndptDIRSTAT_Type())
endptDIRSTAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDIRSTAT.setStatus(_B)
_EndptFTPSRVR_Type=OctetString
_EndptFTPSRVR_Object=MibScalar
endptFTPSRVR=_EndptFTPSRVR_Object((1,3,6,1,4,1,6889,2,69,1,5,11),_EndptFTPSRVR_Type())
endptFTPSRVR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptFTPSRVR.setStatus(_B)
_EndptFTPDIR_Type=DisplayString
_EndptFTPDIR_Object=MibScalar
endptFTPDIR=_EndptFTPDIR_Object((1,3,6,1,4,1,6889,2,69,1,5,12),_EndptFTPDIR_Type())
endptFTPDIR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptFTPDIR.setStatus(_B)
_EndptPHNEMERGNUM_Type=DisplayString
_EndptPHNEMERGNUM_Object=MibScalar
endptPHNEMERGNUM=_EndptPHNEMERGNUM_Object((1,3,6,1,4,1,6889,2,69,1,5,13),_EndptPHNEMERGNUM_Type())
endptPHNEMERGNUM.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPHNEMERGNUM.setStatus(_B)
_EndptPHNNUMOFCA_Type=Integer32
_EndptPHNNUMOFCA_Object=MibScalar
endptPHNNUMOFCA=_EndptPHNNUMOFCA_Object((1,3,6,1,4,1,6889,2,69,1,5,14),_EndptPHNNUMOFCA_Type())
endptPHNNUMOFCA.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPHNNUMOFCA.setStatus(_B)
_EndptPHNNUMOFFB_Type=Integer32
_EndptPHNNUMOFFB_Object=MibScalar
endptPHNNUMOFFB=_EndptPHNNUMOFFB_Object((1,3,6,1,4,1,6889,2,69,1,5,15),_EndptPHNNUMOFFB_Type())
endptPHNNUMOFFB.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPHNNUMOFFB.setStatus(_B)
_EndptWEBCODING_Type=DisplayString
_EndptWEBCODING_Object=MibScalar
endptWEBCODING=_EndptWEBCODING_Object((1,3,6,1,4,1,6889,2,69,1,5,16),_EndptWEBCODING_Type())
endptWEBCODING.setMaxAccess(_A)
if mibBuilder.loadTexts:endptWEBCODING.setStatus(_B)
_EndptWEBEXCEPT_Type=DisplayString
_EndptWEBEXCEPT_Object=MibScalar
endptWEBEXCEPT=_EndptWEBEXCEPT_Object((1,3,6,1,4,1,6889,2,69,1,5,17),_EndptWEBEXCEPT_Type())
endptWEBEXCEPT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptWEBEXCEPT.setStatus(_B)
_EndptWEBHOME_Type=DisplayString
_EndptWEBHOME_Object=MibScalar
endptWEBHOME=_EndptWEBHOME_Object((1,3,6,1,4,1,6889,2,69,1,5,18),_EndptWEBHOME_Type())
endptWEBHOME.setMaxAccess(_A)
if mibBuilder.loadTexts:endptWEBHOME.setStatus(_B)
_EndptWEBPORT_Type=Integer32
_EndptWEBPORT_Object=MibScalar
endptWEBPORT=_EndptWEBPORT_Object((1,3,6,1,4,1,6889,2,69,1,5,19),_EndptWEBPORT_Type())
endptWEBPORT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptWEBPORT.setStatus(_B)
_EndptWEBPROXY_Type=OctetString
_EndptWEBPROXY_Object=MibScalar
endptWEBPROXY=_EndptWEBPROXY_Object((1,3,6,1,4,1,6889,2,69,1,5,20),_EndptWEBPROXY_Type())
endptWEBPROXY.setMaxAccess(_A)
if mibBuilder.loadTexts:endptWEBPROXY.setStatus(_B)
_EndptDIRLDAPPORT_Type=Integer32
_EndptDIRLDAPPORT_Object=MibScalar
endptDIRLDAPPORT=_EndptDIRLDAPPORT_Object((1,3,6,1,4,1,6889,2,69,1,5,21),_EndptDIRLDAPPORT_Type())
endptDIRLDAPPORT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDIRLDAPPORT.setStatus(_B)
_EndptVMLCODING_Type=DisplayString
_EndptVMLCODING_Object=MibScalar
endptVMLCODING=_EndptVMLCODING_Object((1,3,6,1,4,1,6889,2,69,1,5,22),_EndptVMLCODING_Type())
endptVMLCODING.setMaxAccess(_A)
if mibBuilder.loadTexts:endptVMLCODING.setStatus(_B)
_EndptVMLHOME_Type=DisplayString
_EndptVMLHOME_Object=MibScalar
endptVMLHOME=_EndptVMLHOME_Object((1,3,6,1,4,1,6889,2,69,1,5,23),_EndptVMLHOME_Type())
endptVMLHOME.setMaxAccess(_A)
if mibBuilder.loadTexts:endptVMLHOME.setStatus(_B)
_EndptCLACTIVE_Type=Integer32
_EndptCLACTIVE_Object=MibScalar
endptCLACTIVE=_EndptCLACTIVE_Object((1,3,6,1,4,1,6889,2,69,1,5,24),_EndptCLACTIVE_Type())
endptCLACTIVE.setMaxAccess(_A)
if mibBuilder.loadTexts:endptCLACTIVE.setStatus(_C)
_EndptWMLCODING_Type=DisplayString
_EndptWMLCODING_Object=MibScalar
endptWMLCODING=_EndptWMLCODING_Object((1,3,6,1,4,1,6889,2,69,1,5,25),_EndptWMLCODING_Type())
endptWMLCODING.setMaxAccess(_A)
if mibBuilder.loadTexts:endptWMLCODING.setStatus(_C)
_EndptWMLEXCEPT_Type=DisplayString
_EndptWMLEXCEPT_Object=MibScalar
endptWMLEXCEPT=_EndptWMLEXCEPT_Object((1,3,6,1,4,1,6889,2,69,1,5,26),_EndptWMLEXCEPT_Type())
endptWMLEXCEPT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptWMLEXCEPT.setStatus(_B)
_EndptWMLHOME_Type=DisplayString
_EndptWMLHOME_Object=MibScalar
endptWMLHOME=_EndptWMLHOME_Object((1,3,6,1,4,1,6889,2,69,1,5,27),_EndptWMLHOME_Type())
endptWMLHOME.setMaxAccess(_A)
if mibBuilder.loadTexts:endptWMLHOME.setStatus(_B)
_EndptWMLPORT_Type=Integer32
_EndptWMLPORT_Object=MibScalar
endptWMLPORT=_EndptWMLPORT_Object((1,3,6,1,4,1,6889,2,69,1,5,28),_EndptWMLPORT_Type())
endptWMLPORT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptWMLPORT.setStatus(_B)
_EndptWMLPROXY_Type=OctetString
_EndptWMLPROXY_Object=MibScalar
endptWMLPROXY=_EndptWMLPROXY_Object((1,3,6,1,4,1,6889,2,69,1,5,29),_EndptWMLPROXY_Type())
endptWMLPROXY.setMaxAccess(_A)
if mibBuilder.loadTexts:endptWMLPROXY.setStatus(_B)
_EndptCTISTAT_Type=Integer32
_EndptCTISTAT_Object=MibScalar
endptCTISTAT=_EndptCTISTAT_Object((1,3,6,1,4,1,6889,2,69,1,5,30),_EndptCTISTAT_Type())
endptCTISTAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptCTISTAT.setStatus(_B)
_EndptCTIUDPPORT_Type=Integer32
_EndptCTIUDPPORT_Object=MibScalar
endptCTIUDPPORT=_EndptCTIUDPPORT_Object((1,3,6,1,4,1,6889,2,69,1,5,31),_EndptCTIUDPPORT_Type())
endptCTIUDPPORT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptCTIUDPPORT.setStatus(_B)
_EndptSTKSTAT_Type=Integer32
_EndptSTKSTAT_Object=MibScalar
endptSTKSTAT=_EndptSTKSTAT_Object((1,3,6,1,4,1,6889,2,69,1,5,32),_EndptSTKSTAT_Type())
endptSTKSTAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptSTKSTAT.setStatus(_B)
_EndptSUBSCRIBELIST_Type=DisplayString
_EndptSUBSCRIBELIST_Object=MibScalar
endptSUBSCRIBELIST=_EndptSUBSCRIBELIST_Object((1,3,6,1,4,1,6889,2,69,1,5,33),_EndptSUBSCRIBELIST_Type())
endptSUBSCRIBELIST.setMaxAccess(_A)
if mibBuilder.loadTexts:endptSUBSCRIBELIST.setStatus(_B)
_EndptTPSLIST_Type=DisplayString
_EndptTPSLIST_Object=MibScalar
endptTPSLIST=_EndptTPSLIST_Object((1,3,6,1,4,1,6889,2,69,1,5,34),_EndptTPSLIST_Type())
endptTPSLIST.setMaxAccess(_A)
if mibBuilder.loadTexts:endptTPSLIST.setStatus(_B)
_EndptWMLIDLETIME_Type=Integer32
_EndptWMLIDLETIME_Object=MibScalar
endptWMLIDLETIME=_EndptWMLIDLETIME_Object((1,3,6,1,4,1,6889,2,69,1,5,35),_EndptWMLIDLETIME_Type())
endptWMLIDLETIME.setMaxAccess(_A)
if mibBuilder.loadTexts:endptWMLIDLETIME.setStatus(_B)
_EndptWMLIDLEURI_Type=DisplayString
_EndptWMLIDLEURI_Object=MibScalar
endptWMLIDLEURI=_EndptWMLIDLEURI_Object((1,3,6,1,4,1,6889,2,69,1,5,36),_EndptWMLIDLEURI_Type())
endptWMLIDLEURI.setMaxAccess(_A)
if mibBuilder.loadTexts:endptWMLIDLEURI.setStatus(_B)
_EndptAdjuncts_ObjectIdentity=ObjectIdentity
endptAdjuncts=_EndptAdjuncts_ObjectIdentity((1,3,6,1,4,1,6889,2,69,1,6))
_EndptFKEU_Type=Integer32
_EndptFKEU_Object=MibScalar
endptFKEU=_EndptFKEU_Object((1,3,6,1,4,1,6889,2,69,1,6,1),_EndptFKEU_Type())
endptFKEU.setMaxAccess(_A)
if mibBuilder.loadTexts:endptFKEU.setStatus(_B)
_EndptFKEUHEALTH_Type=Integer32
_EndptFKEUHEALTH_Object=MibScalar
endptFKEUHEALTH=_EndptFKEUHEALTH_Object((1,3,6,1,4,1,6889,2,69,1,6,2),_EndptFKEUHEALTH_Type())
endptFKEUHEALTH.setMaxAccess(_A)
if mibBuilder.loadTexts:endptFKEUHEALTH.setStatus(_B)
_EndptSIP_ObjectIdentity=ObjectIdentity
endptSIP=_EndptSIP_ObjectIdentity((1,3,6,1,4,1,6889,2,69,1,7))
_EndptCALLFWDSTAT_Type=Integer32
_EndptCALLFWDSTAT_Object=MibScalar
endptCALLFWDSTAT=_EndptCALLFWDSTAT_Object((1,3,6,1,4,1,6889,2,69,1,7,1),_EndptCALLFWDSTAT_Type())
endptCALLFWDSTAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptCALLFWDSTAT.setStatus(_B)
_EndptCOVERAGEADDR_Type=DisplayString
_EndptCOVERAGEADDR_Object=MibScalar
endptCOVERAGEADDR=_EndptCOVERAGEADDR_Object((1,3,6,1,4,1,6889,2,69,1,7,2),_EndptCOVERAGEADDR_Type())
endptCOVERAGEADDR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptCOVERAGEADDR.setStatus(_B)
_EndptDATETIMEFORMAT_Type=Integer32
_EndptDATETIMEFORMAT_Object=MibScalar
endptDATETIMEFORMAT=_EndptDATETIMEFORMAT_Object((1,3,6,1,4,1,6889,2,69,1,7,3),_EndptDATETIMEFORMAT_Type())
endptDATETIMEFORMAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDATETIMEFORMAT.setStatus(_B)
_EndptMUSICSRVR_Type=DisplayString
_EndptMUSICSRVR_Object=MibScalar
endptMUSICSRVR=_EndptMUSICSRVR_Object((1,3,6,1,4,1,6889,2,69,1,7,4),_EndptMUSICSRVR_Type())
endptMUSICSRVR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptMUSICSRVR.setStatus(_B)
_EndptMUSICSRVRINUSE_Type=IpAddress
_EndptMUSICSRVRINUSE_Object=MibScalar
endptMUSICSRVRINUSE=_EndptMUSICSRVRINUSE_Object((1,3,6,1,4,1,6889,2,69,1,7,5),_EndptMUSICSRVRINUSE_Type())
endptMUSICSRVRINUSE.setMaxAccess(_A)
if mibBuilder.loadTexts:endptMUSICSRVRINUSE.setStatus(_B)
_EndptMWISRVR_Type=DisplayString
_EndptMWISRVR_Object=MibScalar
endptMWISRVR=_EndptMWISRVR_Object((1,3,6,1,4,1,6889,2,69,1,7,6),_EndptMWISRVR_Type())
endptMWISRVR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptMWISRVR.setStatus(_B)
_EndptMWISRVRINUSE_Type=IpAddress
_EndptMWISRVRINUSE_Object=MibScalar
endptMWISRVRINUSE=_EndptMWISRVRINUSE_Object((1,3,6,1,4,1,6889,2,69,1,7,7),_EndptMWISRVRINUSE_Type())
endptMWISRVRINUSE.setMaxAccess(_A)
if mibBuilder.loadTexts:endptMWISRVRINUSE.setStatus(_B)
_EndptREGISTERWAIT_Type=Integer32
_EndptREGISTERWAIT_Object=MibScalar
endptREGISTERWAIT=_EndptREGISTERWAIT_Object((1,3,6,1,4,1,6889,2,69,1,7,8),_EndptREGISTERWAIT_Type())
endptREGISTERWAIT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptREGISTERWAIT.setStatus(_B)
_EndptSIPPROXYSRVR_Type=DisplayString
_EndptSIPPROXYSRVR_Object=MibScalar
endptSIPPROXYSRVR=_EndptSIPPROXYSRVR_Object((1,3,6,1,4,1,6889,2,69,1,7,9),_EndptSIPPROXYSRVR_Type())
endptSIPPROXYSRVR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptSIPPROXYSRVR.setStatus(_B)
_EndptSIPPROXYSRVRINUSE_Type=IpAddress
_EndptSIPPROXYSRVRINUSE_Object=MibScalar
endptSIPPROXYSRVRINUSE=_EndptSIPPROXYSRVRINUSE_Object((1,3,6,1,4,1,6889,2,69,1,7,10),_EndptSIPPROXYSRVRINUSE_Type())
endptSIPPROXYSRVRINUSE.setMaxAccess(_A)
if mibBuilder.loadTexts:endptSIPPROXYSRVRINUSE.setStatus(_B)
_EndptSIPREGISTRAR_Type=DisplayString
_EndptSIPREGISTRAR_Object=MibScalar
endptSIPREGISTRAR=_EndptSIPREGISTRAR_Object((1,3,6,1,4,1,6889,2,69,1,7,11),_EndptSIPREGISTRAR_Type())
endptSIPREGISTRAR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptSIPREGISTRAR.setStatus(_B)
_EndptSIPREGISTRARINUSE_Type=IpAddress
_EndptSIPREGISTRARINUSE_Object=MibScalar
endptSIPREGISTRARINUSE=_EndptSIPREGISTRARINUSE_Object((1,3,6,1,4,1,6889,2,69,1,7,12),_EndptSIPREGISTRARINUSE_Type())
endptSIPREGISTRARINUSE.setMaxAccess(_A)
if mibBuilder.loadTexts:endptSIPREGISTRARINUSE.setStatus(_B)
_EndptSPEAKERSTAT_Type=Integer32
_EndptSPEAKERSTAT_Object=MibScalar
endptSPEAKERSTAT=_EndptSPEAKERSTAT_Object((1,3,6,1,4,1,6889,2,69,1,7,13),_EndptSPEAKERSTAT_Type())
endptSPEAKERSTAT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptSPEAKERSTAT.setStatus(_B)
_EndptSIPPORT_Type=Integer32
_EndptSIPPORT_Object=MibScalar
endptSIPPORT=_EndptSIPPORT_Object((1,3,6,1,4,1,6889,2,69,1,7,14),_EndptSIPPORT_Type())
endptSIPPORT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptSIPPORT.setStatus(_B)
_EndptSIPDOMAIN_Type=DisplayString
_EndptSIPDOMAIN_Object=MibScalar
endptSIPDOMAIN=_EndptSIPDOMAIN_Object((1,3,6,1,4,1,6889,2,69,1,7,15),_EndptSIPDOMAIN_Type())
endptSIPDOMAIN.setMaxAccess(_A)
if mibBuilder.loadTexts:endptSIPDOMAIN.setStatus(_B)
_EndptPHNNUMOFSA_Type=Integer32
_EndptPHNNUMOFSA_Object=MibScalar
endptPHNNUMOFSA=_EndptPHNNUMOFSA_Object((1,3,6,1,4,1,6889,2,69,1,7,16),_EndptPHNNUMOFSA_Type())
endptPHNNUMOFSA.setMaxAccess(_A)
if mibBuilder.loadTexts:endptPHNNUMOFSA.setStatus(_B)
_EndptDIALWAIT_Type=Integer32
_EndptDIALWAIT_Object=MibScalar
endptDIALWAIT=_EndptDIALWAIT_Object((1,3,6,1,4,1,6889,2,69,1,7,17),_EndptDIALWAIT_Type())
endptDIALWAIT.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDIALWAIT.setStatus(_B)
_EndptDIALPLAN_Type=DisplayString
_EndptDIALPLAN_Object=MibScalar
endptDIALPLAN=_EndptDIALPLAN_Object((1,3,6,1,4,1,6889,2,69,1,7,18),_EndptDIALPLAN_Type())
endptDIALPLAN.setMaxAccess(_A)
if mibBuilder.loadTexts:endptDIALPLAN.setStatus(_B)
_EndptCALLFWDADDR_Type=DisplayString
_EndptCALLFWDADDR_Object=MibScalar
endptCALLFWDADDR=_EndptCALLFWDADDR_Object((1,3,6,1,4,1,6889,2,69,1,7,19),_EndptCALLFWDADDR_Type())
endptCALLFWDADDR.setMaxAccess(_A)
if mibBuilder.loadTexts:endptCALLFWDADDR.setStatus(_B)
_EndptCALLFWDDELAY_Type=Integer32
_EndptCALLFWDDELAY_Object=MibScalar
endptCALLFWDDELAY=_EndptCALLFWDDELAY_Object((1,3,6,1,4,1,6889,2,69,1,7,20),_EndptCALLFWDDELAY_Type())
endptCALLFWDDELAY.setMaxAccess(_A)
if mibBuilder.loadTexts:endptCALLFWDDELAY.setStatus(_B)
mibBuilder.exportSymbols(_D,**{'avaya':avaya,'avayaProducts':avayaProducts,'avayaipEndpointProd':avayaipEndpointProd,'avayaMibs':avayaMibs,'avayaipEndpointMIBs':avayaipEndpointMIBs,'endpointMIB':endpointMIB,'endptID':endptID,'endptMARKET':endptMARKET,'endptMODEL':endptMODEL,'endptMCIPADD':endptMCIPADD,'endptMCIPINUSE':endptMCIPINUSE,'endptMCPORT':endptMCPORT,'endptPHONESN':endptPHONESN,'endptPWBCC':endptPWBCC,'endptPWBSN':endptPWBSN,'endptETHERADD':endptETHERADD,'endptESPEED':endptESPEED,'endptIPADD':endptIPADD,'endptDHCPLEASETIME':endptDHCPLEASETIME,'endptDHCPLEASERENEW':endptDHCPLEASERENEW,'endptDHCPLEASEREBIND':endptDHCPLEASEREBIND,'endptGIPADD':endptGIPADD,'endptGIPINUSE':endptGIPINUSE,'endptNETMASK':endptNETMASK,'endptTFTPDIR':endptTFTPDIR,'endptTFTPSRVR':endptTFTPSRVR,'endptTFTPINUSE':endptTFTPINUSE,'endptBOOTNAME':endptBOOTNAME,'endptAPPNAME':endptAPPNAME,'endptSSON':endptSSON,'endptBBURST':endptBBURST,'endptHUBSTAT':endptHUBSTAT,'endptDSCPAUD':endptDSCPAUD,'endptDSCPSIG':endptDSCPSIG,'endptL2Q':endptL2Q,'endptL2QAUD':endptL2QAUD,'endptL2QSIG':endptL2QSIG,'endptL2QVLAN':endptL2QVLAN,'endpt46XXUPGR':endpt46XXUPGR,'endptDNSSRVR':endptDNSSRVR,'endptDNSINUSE':endptDNSINUSE,'endptDOMAIN':endptDOMAIN,'endptRTCPMON':endptRTCPMON,'endptPHY2STAT':endptPHY2STAT,'endptIRSTAT':endptIRSTAT,'endptSMTPSRVR':endptSMTPSRVR,'endptDSPVERSION':endptDSPVERSION,'endptLOGSRVR':endptLOGSRVR,'endptLOGSTAT':endptLOGSTAT,'endptAGCHAND':endptAGCHAND,'endptAGCHEAD':endptAGCHEAD,'endptPHY1STAT':endptPHY1STAT,'endptL2QSTAT':endptL2QSTAT,'endptVLANTEST':endptVLANTEST,'endptPHONECC':endptPHONECC,'endptVLANLIST':endptVLANLIST,'endptAGCSPKR':endptAGCSPKR,'endptHTTPSRVR':endptHTTPSRVR,'endptHTTPDIR':endptHTTPDIR,'endptHTTPPORT':endptHTTPPORT,'endptHTTPUSED':endptHTTPUSED,'endptPROCSTAT':endptPROCSTAT,'endptPROCPSWD':endptPROCPSWD,'endptSIG':endptSIG,'endptGROUP':endptGROUP,'endptSNMPADD':endptSNMPADD,'endptCODESRVR':endptCODESRVR,'endptCODEUSED':endptCODEUSED,'endptSTATIC':endptSTATIC,'endptTLSSRVR':endptTLSSRVR,'endptTLSUSED':endptTLSUSED,'endptCNAPORT':endptCNAPORT,'endptCNASRVR':endptCNASRVR,'endptDSTOFFSET':endptDSTOFFSET,'endptDSTSTART':endptDSTSTART,'endptDSTSTOP':endptDSTSTOP,'endptGMTOFFSET':endptGMTOFFSET,'endptSNTPSRVR':endptSNTPSRVR,'endptBAKLIGHTOFF':endptBAKLIGHTOFF,'endptDOT1X':endptDOT1X,'endptAUDIOENV':endptAUDIOENV,'endptAUDIOSTHD':endptAUDIOSTHD,'endptAUDIOSTHS':endptAUDIOSTHS,'endptDHCPINUSE':endptDHCPINUSE,'endptDHCPLEASEEXP':endptDHCPLEASEEXP,'endptDHCPSTD':endptDHCPSTD,'endptDHCPT1REM':endptDHCPT1REM,'endptDHCPT2REM':endptDHCPT2REM,'endptICMPDU':endptICMPDU,'endptICMPRED':endptICMPRED,'endptSSONCONTENT':endptSSONCONTENT,'endptBRURI':endptBRURI,'endptNVM':endptNVM,'endptNVMCIPADD':endptNVMCIPADD,'endptNVMCPORT':endptNVMCPORT,'endptNVIPADD':endptNVIPADD,'endptNVGIPADD':endptNVGIPADD,'endptNVNETMASK':endptNVNETMASK,'endptNVTFTPSRVR':endptNVTFTPSRVR,'endptNVSSON':endptNVSSON,'endptNVBBURST':endptNVBBURST,'endptNVHUBSTAT':endptNVHUBSTAT,'endptNVDSCPAUD':endptNVDSCPAUD,'endptNVDSCPSIG':endptNVDSCPSIG,'endptNVL2Q':endptNVL2Q,'endptNVL2QAUD':endptNVL2QAUD,'endptNVL2QSIG':endptNVL2QSIG,'endptNVL2QVLAN':endptNVL2QVLAN,'endptNVPHY2STAT':endptNVPHY2STAT,'endptNVLOGSTAT':endptNVLOGSTAT,'endptNVAGCHAND':endptNVAGCHAND,'endptNVAGCHEAD':endptNVAGCHEAD,'endptNVIRSTAT':endptNVIRSTAT,'endptNVPHY1STAT':endptNVPHY1STAT,'endptNVVLANTEST':endptNVVLANTEST,'endptNVVLANLIST':endptNVVLANLIST,'endptNVAGCSPKR':endptNVAGCSPKR,'endptNVHTTPSRVR':endptNVHTTPSRVR,'endptNVAUTH':endptNVAUTH,'endptNVFILESRVR':endptNVFILESRVR,'endptNVALERT':endptNVALERT,'endptNVCHADDR':endptNVCHADDR,'endptNVCONTRAST':endptNVCONTRAST,'endptMaintenance':endptMaintenance,'endptUPGRADESCRIPT':endptUPGRADESCRIPT,'endptAPPINUSE':endptAPPINUSE,'endptAPPSTAT':endptAPPSTAT,'endptRecentLog':endptRecentLog,'endptRecentLogEntry':endptRecentLogEntry,_E:endptRecentLogText,'endptResetLog':endptResetLog,'endptResetLogEntry':endptResetLogEntry,_F:endptResetLogText,'endptDEFINITY':endptDEFINITY,'endptPORTAUD':endptPORTAUD,'endptPORTSIG':endptPORTSIG,'endptFEIPADD':endptFEIPADD,'endptFEPORT':endptFEPORT,'endptCODECR':endptCODECR,'endptCODECT':endptCODECT,'endptJCPC':endptJCPC,'endptTMSEC':endptTMSEC,'endptNVPHONEXT':endptNVPHONEXT,'endptL2QBBE':endptL2QBBE,'endptDSCPBBE':endptDSCPBBE,'endptRTCPCONT':endptRTCPCONT,'endptRTCPFLOW':endptRTCPFLOW,'endptRSVPCONT':endptRSVPCONT,'endptRSVPRFRSH':endptRSVPRFRSH,'endptRSVPRTRY':endptRSVPRTRY,'endptRSVPPROF':endptRSVPPROF,'endptPHNCC':endptPHNCC,'endptPHNDPLENGTH':endptPHNDPLENGTH,'endptPHNIC':endptPHNIC,'endptPHNLD':endptPHNLD,'endptPHNLDLENGTH':endptPHNLDLENGTH,'endptPHNOL':endptPHNOL,'endptNTWKAUDIO':endptNTWKAUDIO,'endptENHDIALSTAT':endptENHDIALSTAT,'endptRESTORESTAT':endptRESTORESTAT,'endptFTPUSERSTAT':endptFTPUSERSTAT,'endptRASGkList':endptRASGkList,'endptRASGkEntry':endptRASGkEntry,_G:endptRASGkEntryData,'endptAdvApps':endptAdvApps,'endptCIBURL':endptCIBURL,'endptDIRSRVR':endptDIRSRVR,'endptDIRTOPDN':endptDIRTOPDN,'endptDIRFULLNAME':endptDIRFULLNAME,'endptDIRTELNUM':endptDIRTELNUM,'endptDIRSRCHTIME':endptDIRSRCHTIME,'endptDIRSRVRPWD':endptDIRSRVRPWD,'endptDIRUSERID':endptDIRUSERID,'endptDIRCODING':endptDIRCODING,'endptDIRSTAT':endptDIRSTAT,'endptFTPSRVR':endptFTPSRVR,'endptFTPDIR':endptFTPDIR,'endptPHNEMERGNUM':endptPHNEMERGNUM,'endptPHNNUMOFCA':endptPHNNUMOFCA,'endptPHNNUMOFFB':endptPHNNUMOFFB,'endptWEBCODING':endptWEBCODING,'endptWEBEXCEPT':endptWEBEXCEPT,'endptWEBHOME':endptWEBHOME,'endptWEBPORT':endptWEBPORT,'endptWEBPROXY':endptWEBPROXY,'endptDIRLDAPPORT':endptDIRLDAPPORT,'endptVMLCODING':endptVMLCODING,'endptVMLHOME':endptVMLHOME,'endptCLACTIVE':endptCLACTIVE,'endptWMLCODING':endptWMLCODING,'endptWMLEXCEPT':endptWMLEXCEPT,'endptWMLHOME':endptWMLHOME,'endptWMLPORT':endptWMLPORT,'endptWMLPROXY':endptWMLPROXY,'endptCTISTAT':endptCTISTAT,'endptCTIUDPPORT':endptCTIUDPPORT,'endptSTKSTAT':endptSTKSTAT,'endptSUBSCRIBELIST':endptSUBSCRIBELIST,'endptTPSLIST':endptTPSLIST,'endptWMLIDLETIME':endptWMLIDLETIME,'endptWMLIDLEURI':endptWMLIDLEURI,'endptAdjuncts':endptAdjuncts,'endptFKEU':endptFKEU,'endptFKEUHEALTH':endptFKEUHEALTH,'endptSIP':endptSIP,'endptCALLFWDSTAT':endptCALLFWDSTAT,'endptCOVERAGEADDR':endptCOVERAGEADDR,'endptDATETIMEFORMAT':endptDATETIMEFORMAT,'endptMUSICSRVR':endptMUSICSRVR,'endptMUSICSRVRINUSE':endptMUSICSRVRINUSE,'endptMWISRVR':endptMWISRVR,'endptMWISRVRINUSE':endptMWISRVRINUSE,'endptREGISTERWAIT':endptREGISTERWAIT,'endptSIPPROXYSRVR':endptSIPPROXYSRVR,'endptSIPPROXYSRVRINUSE':endptSIPPROXYSRVRINUSE,'endptSIPREGISTRAR':endptSIPREGISTRAR,'endptSIPREGISTRARINUSE':endptSIPREGISTRARINUSE,'endptSPEAKERSTAT':endptSPEAKERSTAT,'endptSIPPORT':endptSIPPORT,'endptSIPDOMAIN':endptSIPDOMAIN,'endptPHNNUMOFSA':endptPHNNUMOFSA,'endptDIALWAIT':endptDIALWAIT,'endptDIALPLAN':endptDIALPLAN,'endptCALLFWDADDR':endptCALLFWDADDR,'endptCALLFWDDELAY':endptCALLFWDDELAY})