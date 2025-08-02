_G='dsMonitorSipPortIndex'
_F='dsSipPortIndex'
_E='dsSipSlotIndex'
_D='read-only'
_C='DASAN-ACCESS-SLOT-SIP-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dasanMgmt,=mibBuilder.importSymbols('DASAN-SMI','dasanMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
AutonomousType,DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','RowStatus','TextualConvention','TestAndIncr','TimeStamp')
dasanAccessMib=ModuleIdentity((1,3,6,1,4,1,6296,9,100))
if mibBuilder.loadTexts:dasanAccessMib.setRevisions(('2005-02-11 21:00',))
_DasanAccGatewayMIBObjects_ObjectIdentity=ObjectIdentity
dasanAccGatewayMIBObjects=_DasanAccGatewayMIBObjects_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2))
_DsAccGwySip_ObjectIdentity=ObjectIdentity
dsAccGwySip=_DsAccGwySip_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,4))
_DsAccGwySipConfiguration_ObjectIdentity=ObjectIdentity
dsAccGwySipConfiguration=_DsAccGwySipConfiguration_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,4,1))
_DsAccGwyConfigSipSlot_ObjectIdentity=ObjectIdentity
dsAccGwyConfigSipSlot=_DsAccGwyConfigSipSlot_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,4,1,1))
_DsAccGwyConfigSipSlotTable_Object=MibTable
dsAccGwyConfigSipSlotTable=_DsAccGwyConfigSipSlotTable_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1))
if mibBuilder.loadTexts:dsAccGwyConfigSipSlotTable.setStatus(_A)
_DsAccGwyConfigSipSlotEntry_Object=MibTableRow
dsAccGwyConfigSipSlotEntry=_DsAccGwyConfigSipSlotEntry_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1,1))
dsAccGwyConfigSipSlotEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:dsAccGwyConfigSipSlotEntry.setStatus(_A)
_DsSipSlotIndex_Type=Integer32
_DsSipSlotIndex_Object=MibTableColumn
dsSipSlotIndex=_DsSipSlotIndex_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1,1,1),_DsSipSlotIndex_Type())
dsSipSlotIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dsSipSlotIndex.setStatus(_A)
_DsSipSlotDomain_Type=DisplayString
_DsSipSlotDomain_Object=MibTableColumn
dsSipSlotDomain=_DsSipSlotDomain_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1,1,2),_DsSipSlotDomain_Type())
dsSipSlotDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipSlotDomain.setStatus(_A)
_DsSipSlotSockMode_Type=Integer32
_DsSipSlotSockMode_Object=MibTableColumn
dsSipSlotSockMode=_DsSipSlotSockMode_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1,1,3),_DsSipSlotSockMode_Type())
dsSipSlotSockMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipSlotSockMode.setStatus(_A)
_DsSipSlotSipPort_Type=Integer32
_DsSipSlotSipPort_Object=MibTableColumn
dsSipSlotSipPort=_DsSipSlotSipPort_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1,1,4),_DsSipSlotSipPort_Type())
dsSipSlotSipPort.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipSlotSipPort.setStatus(_A)
_DsSipSlotProxyAddr1_Type=DisplayString
_DsSipSlotProxyAddr1_Object=MibTableColumn
dsSipSlotProxyAddr1=_DsSipSlotProxyAddr1_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1,1,5),_DsSipSlotProxyAddr1_Type())
dsSipSlotProxyAddr1.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipSlotProxyAddr1.setStatus(_A)
_DsSipSlotProxyPort1_Type=Integer32
_DsSipSlotProxyPort1_Object=MibTableColumn
dsSipSlotProxyPort1=_DsSipSlotProxyPort1_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1,1,6),_DsSipSlotProxyPort1_Type())
dsSipSlotProxyPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipSlotProxyPort1.setStatus(_A)
_DsSipSlotProxyAddr2_Type=DisplayString
_DsSipSlotProxyAddr2_Object=MibTableColumn
dsSipSlotProxyAddr2=_DsSipSlotProxyAddr2_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1,1,7),_DsSipSlotProxyAddr2_Type())
dsSipSlotProxyAddr2.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipSlotProxyAddr2.setStatus(_A)
_DsSipSlotProxyPort2_Type=Integer32
_DsSipSlotProxyPort2_Object=MibTableColumn
dsSipSlotProxyPort2=_DsSipSlotProxyPort2_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1,1,8),_DsSipSlotProxyPort2_Type())
dsSipSlotProxyPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipSlotProxyPort2.setStatus(_A)
_DsSipSlotProxyAddr3_Type=DisplayString
_DsSipSlotProxyAddr3_Object=MibTableColumn
dsSipSlotProxyAddr3=_DsSipSlotProxyAddr3_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1,1,9),_DsSipSlotProxyAddr3_Type())
dsSipSlotProxyAddr3.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipSlotProxyAddr3.setStatus(_A)
_DsSipSlotProxyPort3_Type=Integer32
_DsSipSlotProxyPort3_Object=MibTableColumn
dsSipSlotProxyPort3=_DsSipSlotProxyPort3_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1,1,10),_DsSipSlotProxyPort3_Type())
dsSipSlotProxyPort3.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipSlotProxyPort3.setStatus(_A)
_DsSipSlotHuntMapItem_Type=DisplayString
_DsSipSlotHuntMapItem_Object=MibTableColumn
dsSipSlotHuntMapItem=_DsSipSlotHuntMapItem_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1,1,11),_DsSipSlotHuntMapItem_Type())
dsSipSlotHuntMapItem.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipSlotHuntMapItem.setStatus(_A)
_DsSipSlotDigitMapItem_Type=DisplayString
_DsSipSlotDigitMapItem_Object=MibTableColumn
dsSipSlotDigitMapItem=_DsSipSlotDigitMapItem_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1,1,12),_DsSipSlotDigitMapItem_Type())
dsSipSlotDigitMapItem.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipSlotDigitMapItem.setStatus(_A)
_DsSipSlotSigProvisionTO_Type=Integer32
_DsSipSlotSigProvisionTO_Object=MibTableColumn
dsSipSlotSigProvisionTO=_DsSipSlotSigProvisionTO_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1,1,13),_DsSipSlotSigProvisionTO_Type())
dsSipSlotSigProvisionTO.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipSlotSigProvisionTO.setStatus(_A)
_DsSipSlotSigAleringTO_Type=Integer32
_DsSipSlotSigAleringTO_Object=MibTableColumn
dsSipSlotSigAleringTO=_DsSipSlotSigAleringTO_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1,1,14),_DsSipSlotSigAleringTO_Type())
dsSipSlotSigAleringTO.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipSlotSigAleringTO.setStatus(_A)
_DsSipSlotSigConnectTO_Type=Integer32
_DsSipSlotSigConnectTO_Object=MibTableColumn
dsSipSlotSigConnectTO=_DsSipSlotSigConnectTO_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1,1,15),_DsSipSlotSigConnectTO_Type())
dsSipSlotSigConnectTO.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipSlotSigConnectTO.setStatus(_A)
_DsSipSlotHookOffTO_Type=Integer32
_DsSipSlotHookOffTO_Object=MibTableColumn
dsSipSlotHookOffTO=_DsSipSlotHookOffTO_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1,1,16),_DsSipSlotHookOffTO_Type())
dsSipSlotHookOffTO.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipSlotHookOffTO.setStatus(_A)
_DsSipSlotHookOnTO_Type=Integer32
_DsSipSlotHookOnTO_Object=MibTableColumn
dsSipSlotHookOnTO=_DsSipSlotHookOnTO_Object((1,3,6,1,4,1,6296,9,100,2,4,1,1,1,1,17),_DsSipSlotHookOnTO_Type())
dsSipSlotHookOnTO.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipSlotHookOnTO.setStatus(_A)
_DsAccGwyConfigSipPort_ObjectIdentity=ObjectIdentity
dsAccGwyConfigSipPort=_DsAccGwyConfigSipPort_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,4,1,2))
_DsAccGwyConfigSipPortTable_Object=MibTable
dsAccGwyConfigSipPortTable=_DsAccGwyConfigSipPortTable_Object((1,3,6,1,4,1,6296,9,100,2,4,1,2,1))
if mibBuilder.loadTexts:dsAccGwyConfigSipPortTable.setStatus(_A)
_DsAccGwyConfigSipPortEntry_Object=MibTableRow
dsAccGwyConfigSipPortEntry=_DsAccGwyConfigSipPortEntry_Object((1,3,6,1,4,1,6296,9,100,2,4,1,2,1,1))
dsAccGwyConfigSipPortEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:dsAccGwyConfigSipPortEntry.setStatus(_A)
_DsSipPortIndex_Type=Integer32
_DsSipPortIndex_Object=MibTableColumn
dsSipPortIndex=_DsSipPortIndex_Object((1,3,6,1,4,1,6296,9,100,2,4,1,2,1,1,1),_DsSipPortIndex_Type())
dsSipPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dsSipPortIndex.setStatus(_A)
_DsSipPortMyTel_Type=DisplayString
_DsSipPortMyTel_Object=MibTableColumn
dsSipPortMyTel=_DsSipPortMyTel_Object((1,3,6,1,4,1,6296,9,100,2,4,1,2,1,1,2),_DsSipPortMyTel_Type())
dsSipPortMyTel.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipPortMyTel.setStatus(_A)
_DsSipPortURI_Type=DisplayString
_DsSipPortURI_Object=MibTableColumn
dsSipPortURI=_DsSipPortURI_Object((1,3,6,1,4,1,6296,9,100,2,4,1,2,1,1,3),_DsSipPortURI_Type())
dsSipPortURI.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipPortURI.setStatus(_A)
_DsSipPortContactURI_Type=DisplayString
_DsSipPortContactURI_Object=MibTableColumn
dsSipPortContactURI=_DsSipPortContactURI_Object((1,3,6,1,4,1,6296,9,100,2,4,1,2,1,1,4),_DsSipPortContactURI_Type())
dsSipPortContactURI.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipPortContactURI.setStatus(_A)
_DsSipPortDisplayName_Type=DisplayString
_DsSipPortDisplayName_Object=MibTableColumn
dsSipPortDisplayName=_DsSipPortDisplayName_Object((1,3,6,1,4,1,6296,9,100,2,4,1,2,1,1,5),_DsSipPortDisplayName_Type())
dsSipPortDisplayName.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipPortDisplayName.setStatus(_A)
_DsSipPortUserName_Type=DisplayString
_DsSipPortUserName_Object=MibTableColumn
dsSipPortUserName=_DsSipPortUserName_Object((1,3,6,1,4,1,6296,9,100,2,4,1,2,1,1,6),_DsSipPortUserName_Type())
dsSipPortUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipPortUserName.setStatus(_A)
_DsSipPortUserID_Type=DisplayString
_DsSipPortUserID_Object=MibTableColumn
dsSipPortUserID=_DsSipPortUserID_Object((1,3,6,1,4,1,6296,9,100,2,4,1,2,1,1,7),_DsSipPortUserID_Type())
dsSipPortUserID.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipPortUserID.setStatus(_A)
_DsSipPortUserPW_Type=DisplayString
_DsSipPortUserPW_Object=MibTableColumn
dsSipPortUserPW=_DsSipPortUserPW_Object((1,3,6,1,4,1,6296,9,100,2,4,1,2,1,1,8),_DsSipPortUserPW_Type())
dsSipPortUserPW.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipPortUserPW.setStatus(_A)
_DsSipPortRealM_Type=DisplayString
_DsSipPortRealM_Object=MibTableColumn
dsSipPortRealM=_DsSipPortRealM_Object((1,3,6,1,4,1,6296,9,100,2,4,1,2,1,1,9),_DsSipPortRealM_Type())
dsSipPortRealM.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipPortRealM.setStatus(_A)
_DsSipPortExpiry_Type=Integer32
_DsSipPortExpiry_Object=MibTableColumn
dsSipPortExpiry=_DsSipPortExpiry_Object((1,3,6,1,4,1,6296,9,100,2,4,1,2,1,1,10),_DsSipPortExpiry_Type())
dsSipPortExpiry.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSipPortExpiry.setStatus(_A)
_DsAccGwySipMonitor_ObjectIdentity=ObjectIdentity
dsAccGwySipMonitor=_DsAccGwySipMonitor_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,4,2))
_DsAccGwyMonitorSipPort_ObjectIdentity=ObjectIdentity
dsAccGwyMonitorSipPort=_DsAccGwyMonitorSipPort_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,4,2,1))
_DsAccGwyMonitorSipPortTable_Object=MibTable
dsAccGwyMonitorSipPortTable=_DsAccGwyMonitorSipPortTable_Object((1,3,6,1,4,1,6296,9,100,2,4,2,1,1))
if mibBuilder.loadTexts:dsAccGwyMonitorSipPortTable.setStatus(_A)
_DsAccGwyMonitorSipPortEntry_Object=MibTableRow
dsAccGwyMonitorSipPortEntry=_DsAccGwyMonitorSipPortEntry_Object((1,3,6,1,4,1,6296,9,100,2,4,2,1,1,1))
dsAccGwyMonitorSipPortEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:dsAccGwyMonitorSipPortEntry.setStatus(_A)
_DsMonitorSipPortIndex_Type=Integer32
_DsMonitorSipPortIndex_Object=MibTableColumn
dsMonitorSipPortIndex=_DsMonitorSipPortIndex_Object((1,3,6,1,4,1,6296,9,100,2,4,2,1,1,1,1),_DsMonitorSipPortIndex_Type())
dsMonitorSipPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dsMonitorSipPortIndex.setStatus(_A)
_DsSipPortProxyStatus_Type=Integer32
_DsSipPortProxyStatus_Object=MibTableColumn
dsSipPortProxyStatus=_DsSipPortProxyStatus_Object((1,3,6,1,4,1,6296,9,100,2,4,2,1,1,1,2),_DsSipPortProxyStatus_Type())
dsSipPortProxyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dsSipPortProxyStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'dasanAccessMib':dasanAccessMib,'dasanAccGatewayMIBObjects':dasanAccGatewayMIBObjects,'dsAccGwySip':dsAccGwySip,'dsAccGwySipConfiguration':dsAccGwySipConfiguration,'dsAccGwyConfigSipSlot':dsAccGwyConfigSipSlot,'dsAccGwyConfigSipSlotTable':dsAccGwyConfigSipSlotTable,'dsAccGwyConfigSipSlotEntry':dsAccGwyConfigSipSlotEntry,_E:dsSipSlotIndex,'dsSipSlotDomain':dsSipSlotDomain,'dsSipSlotSockMode':dsSipSlotSockMode,'dsSipSlotSipPort':dsSipSlotSipPort,'dsSipSlotProxyAddr1':dsSipSlotProxyAddr1,'dsSipSlotProxyPort1':dsSipSlotProxyPort1,'dsSipSlotProxyAddr2':dsSipSlotProxyAddr2,'dsSipSlotProxyPort2':dsSipSlotProxyPort2,'dsSipSlotProxyAddr3':dsSipSlotProxyAddr3,'dsSipSlotProxyPort3':dsSipSlotProxyPort3,'dsSipSlotHuntMapItem':dsSipSlotHuntMapItem,'dsSipSlotDigitMapItem':dsSipSlotDigitMapItem,'dsSipSlotSigProvisionTO':dsSipSlotSigProvisionTO,'dsSipSlotSigAleringTO':dsSipSlotSigAleringTO,'dsSipSlotSigConnectTO':dsSipSlotSigConnectTO,'dsSipSlotHookOffTO':dsSipSlotHookOffTO,'dsSipSlotHookOnTO':dsSipSlotHookOnTO,'dsAccGwyConfigSipPort':dsAccGwyConfigSipPort,'dsAccGwyConfigSipPortTable':dsAccGwyConfigSipPortTable,'dsAccGwyConfigSipPortEntry':dsAccGwyConfigSipPortEntry,_F:dsSipPortIndex,'dsSipPortMyTel':dsSipPortMyTel,'dsSipPortURI':dsSipPortURI,'dsSipPortContactURI':dsSipPortContactURI,'dsSipPortDisplayName':dsSipPortDisplayName,'dsSipPortUserName':dsSipPortUserName,'dsSipPortUserID':dsSipPortUserID,'dsSipPortUserPW':dsSipPortUserPW,'dsSipPortRealM':dsSipPortRealM,'dsSipPortExpiry':dsSipPortExpiry,'dsAccGwySipMonitor':dsAccGwySipMonitor,'dsAccGwyMonitorSipPort':dsAccGwyMonitorSipPort,'dsAccGwyMonitorSipPortTable':dsAccGwyMonitorSipPortTable,'dsAccGwyMonitorSipPortEntry':dsAccGwyMonitorSipPortEntry,_G:dsMonitorSipPortIndex,'dsSipPortProxyStatus':dsSipPortProxyStatus})