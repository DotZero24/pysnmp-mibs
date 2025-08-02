_A7='ceExtUsbModemNotifControlGroup'
_A6='ceExtUsbModemNotificationsGroup'
_A5='ceExtUSBModemGroup'
_A4='ceExtUSBModemPlugOutNotif'
_A3='ceExtUSBModemPlugInNotif'
_A2='ceExtBreakOutPortRemoved'
_A1='ceExtBreakOutPortInserted'
_A0='ceExtEntDoorOpenNotif'
_z='ceExtEntDoorCloseNotif'
_y='ceExtHCNVRAMUsed'
_x='ceExtHCNVRAMSize'
_w='ceExtNVRAMUsedOverflow'
_v='ceExtNVRAMSizeOverflow'
_u='ceExtEntUsbModemNotifEnable'
_t='ceExtUSBModemSignalStrength'
_s='ceExtUSBModemServiceProvider'
_r='ceExtUSBModemIMSI'
_q='ceExtUSBModemIMEI'
_p='ceExtEntBreakOutPortNotifEnable'
_o='ceExtEntDoorNotifEnable'
_n='ceExtHCProcessorRam'
_m='ceExtProcessorRamOverflow'
_l='ceEntPhysicalSecondSerialNum'
_k='ceExtKickstartImageList'
_j='ceExtEntityLEDColor'
_i='ceExtSysBootImageList'
_h='ceExtConfigRegNext'
_g='ceExtConfigRegister'
_f='ceExtNVRAMUsed'
_e='ceExtNVRAMSize'
_d='ceExtProcessorRam'
_c='ceExtEntPhysicalEntry'
_b='ceExtEntityLEDType'
_a='ceExtBreakOutPortNotifControlGroup'
_Z='ceExtBreakOutPortNotifGroup'
_Y='BootImageList'
_X='Integer32'
_W='ceExtEntDoorNotifControlGroup'
_V='ceExtEntDoorNotifGroup'
_U='TruthValue'
_T='ceExtPhyProcessorHCGroup'
_S='ceExtPhyProcessorOverflowGroup'
_R='entPhysicalName'
_Q='entPhysicalIndex'
_P='entPhysicalDescr'
_O='entPhysicalContainedIn'
_N='ciscoExtEntityPhysicalGroup'
_M='deprecated'
_L='read-write'
_K='SnmpAdminString'
_J='ceExtSysBootImageListGroupRev1'
_I='ciscoEntityExtLEDGroup'
_H='ceExtSysBootImageListGroup'
_G='ciscoEntityExtConfigRegGroup'
_F='ceExtPhysicalProcessorGroup'
_E='bytes'
_D='read-only'
_C='ENTITY-MIB'
_B='current'
_A='CISCO-ENTITY-EXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
Unsigned64,=mibBuilder.importSymbols('CISCO-TC','Unsigned64')
entPhysicalContainedIn,entPhysicalDescr,entPhysicalEntry,entPhysicalIndex,entPhysicalName=mibBuilder.importSymbols(_C,_O,_P,'entPhysicalEntry',_Q,_R)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_X,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_U)
ciscoEntityExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,195))
if mibBuilder.loadTexts:ciscoEntityExtMIB.setRevisions(('2018-04-04 00:00','2015-04-17 00:00','2014-09-12 00:00','2014-03-27 00:00','2013-08-06 00:00','2013-08-05 00:00','2008-11-24 00:00','2004-07-06 00:00','2004-03-03 00:00','2004-01-26 00:00','2003-08-24 00:00','2001-05-17 00:00','2001-04-05 00:00'))
class ConfigRegisterValue(TextualConvention,OctetString):status=_B;displayHint='2x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class BootImageList(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CiscoEntityExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoEntityExtMIBObjects=_CiscoEntityExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,195,1))
_CeExtPhysicalProcessorTable_Object=MibTable
ceExtPhysicalProcessorTable=_CeExtPhysicalProcessorTable_Object((1,3,6,1,4,1,9,9,195,1,1))
if mibBuilder.loadTexts:ceExtPhysicalProcessorTable.setStatus(_B)
_CeExtPhysicalProcessorEntry_Object=MibTableRow
ceExtPhysicalProcessorEntry=_CeExtPhysicalProcessorEntry_Object((1,3,6,1,4,1,9,9,195,1,1,1))
ceExtPhysicalProcessorEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:ceExtPhysicalProcessorEntry.setStatus(_B)
_CeExtProcessorRam_Type=Unsigned32
_CeExtProcessorRam_Object=MibTableColumn
ceExtProcessorRam=_CeExtProcessorRam_Object((1,3,6,1,4,1,9,9,195,1,1,1,1),_CeExtProcessorRam_Type())
ceExtProcessorRam.setMaxAccess(_D)
if mibBuilder.loadTexts:ceExtProcessorRam.setStatus(_B)
if mibBuilder.loadTexts:ceExtProcessorRam.setUnits(_E)
_CeExtNVRAMSize_Type=Unsigned32
_CeExtNVRAMSize_Object=MibTableColumn
ceExtNVRAMSize=_CeExtNVRAMSize_Object((1,3,6,1,4,1,9,9,195,1,1,1,2),_CeExtNVRAMSize_Type())
ceExtNVRAMSize.setMaxAccess(_D)
if mibBuilder.loadTexts:ceExtNVRAMSize.setStatus(_B)
if mibBuilder.loadTexts:ceExtNVRAMSize.setUnits(_E)
_CeExtNVRAMUsed_Type=Unsigned32
_CeExtNVRAMUsed_Object=MibTableColumn
ceExtNVRAMUsed=_CeExtNVRAMUsed_Object((1,3,6,1,4,1,9,9,195,1,1,1,3),_CeExtNVRAMUsed_Type())
ceExtNVRAMUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:ceExtNVRAMUsed.setStatus(_B)
if mibBuilder.loadTexts:ceExtNVRAMUsed.setUnits(_E)
_CeExtProcessorRamOverflow_Type=Unsigned32
_CeExtProcessorRamOverflow_Object=MibTableColumn
ceExtProcessorRamOverflow=_CeExtProcessorRamOverflow_Object((1,3,6,1,4,1,9,9,195,1,1,1,4),_CeExtProcessorRamOverflow_Type())
ceExtProcessorRamOverflow.setMaxAccess(_D)
if mibBuilder.loadTexts:ceExtProcessorRamOverflow.setStatus(_B)
if mibBuilder.loadTexts:ceExtProcessorRamOverflow.setUnits(_E)
_CeExtHCProcessorRam_Type=Unsigned64
_CeExtHCProcessorRam_Object=MibTableColumn
ceExtHCProcessorRam=_CeExtHCProcessorRam_Object((1,3,6,1,4,1,9,9,195,1,1,1,5),_CeExtHCProcessorRam_Type())
ceExtHCProcessorRam.setMaxAccess(_D)
if mibBuilder.loadTexts:ceExtHCProcessorRam.setStatus(_B)
if mibBuilder.loadTexts:ceExtHCProcessorRam.setUnits(_E)
_CeExtNVRAMSizeOverflow_Type=Unsigned32
_CeExtNVRAMSizeOverflow_Object=MibTableColumn
ceExtNVRAMSizeOverflow=_CeExtNVRAMSizeOverflow_Object((1,3,6,1,4,1,9,9,195,1,1,1,6),_CeExtNVRAMSizeOverflow_Type())
ceExtNVRAMSizeOverflow.setMaxAccess(_D)
if mibBuilder.loadTexts:ceExtNVRAMSizeOverflow.setStatus(_B)
if mibBuilder.loadTexts:ceExtNVRAMSizeOverflow.setUnits(_E)
_CeExtHCNVRAMSize_Type=Unsigned64
_CeExtHCNVRAMSize_Object=MibTableColumn
ceExtHCNVRAMSize=_CeExtHCNVRAMSize_Object((1,3,6,1,4,1,9,9,195,1,1,1,7),_CeExtHCNVRAMSize_Type())
ceExtHCNVRAMSize.setMaxAccess(_D)
if mibBuilder.loadTexts:ceExtHCNVRAMSize.setStatus(_B)
if mibBuilder.loadTexts:ceExtHCNVRAMSize.setUnits(_E)
_CeExtNVRAMUsedOverflow_Type=Unsigned32
_CeExtNVRAMUsedOverflow_Object=MibTableColumn
ceExtNVRAMUsedOverflow=_CeExtNVRAMUsedOverflow_Object((1,3,6,1,4,1,9,9,195,1,1,1,8),_CeExtNVRAMUsedOverflow_Type())
ceExtNVRAMUsedOverflow.setMaxAccess(_D)
if mibBuilder.loadTexts:ceExtNVRAMUsedOverflow.setStatus(_B)
if mibBuilder.loadTexts:ceExtNVRAMUsedOverflow.setUnits(_E)
_CeExtHCNVRAMUsed_Type=Unsigned64
_CeExtHCNVRAMUsed_Object=MibTableColumn
ceExtHCNVRAMUsed=_CeExtHCNVRAMUsed_Object((1,3,6,1,4,1,9,9,195,1,1,1,9),_CeExtHCNVRAMUsed_Type())
ceExtHCNVRAMUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:ceExtHCNVRAMUsed.setStatus(_B)
if mibBuilder.loadTexts:ceExtHCNVRAMUsed.setUnits(_E)
_CeExtConfigRegTable_Object=MibTable
ceExtConfigRegTable=_CeExtConfigRegTable_Object((1,3,6,1,4,1,9,9,195,1,2))
if mibBuilder.loadTexts:ceExtConfigRegTable.setStatus(_B)
_CeExtConfigRegEntry_Object=MibTableRow
ceExtConfigRegEntry=_CeExtConfigRegEntry_Object((1,3,6,1,4,1,9,9,195,1,2,1))
ceExtConfigRegEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:ceExtConfigRegEntry.setStatus(_B)
_CeExtConfigRegister_Type=ConfigRegisterValue
_CeExtConfigRegister_Object=MibTableColumn
ceExtConfigRegister=_CeExtConfigRegister_Object((1,3,6,1,4,1,9,9,195,1,2,1,1),_CeExtConfigRegister_Type())
ceExtConfigRegister.setMaxAccess(_D)
if mibBuilder.loadTexts:ceExtConfigRegister.setStatus(_B)
_CeExtConfigRegNext_Type=ConfigRegisterValue
_CeExtConfigRegNext_Object=MibTableColumn
ceExtConfigRegNext=_CeExtConfigRegNext_Object((1,3,6,1,4,1,9,9,195,1,2,1,2),_CeExtConfigRegNext_Type())
ceExtConfigRegNext.setMaxAccess(_L)
if mibBuilder.loadTexts:ceExtConfigRegNext.setStatus(_B)
class _CeExtSysBootImageList_Type(BootImageList):defaultValue=OctetString('')
_CeExtSysBootImageList_Type.__name__=_Y
_CeExtSysBootImageList_Object=MibTableColumn
ceExtSysBootImageList=_CeExtSysBootImageList_Object((1,3,6,1,4,1,9,9,195,1,2,1,3),_CeExtSysBootImageList_Type())
ceExtSysBootImageList.setMaxAccess(_L)
if mibBuilder.loadTexts:ceExtSysBootImageList.setStatus(_B)
class _CeExtKickstartImageList_Type(BootImageList):defaultValue=OctetString('')
_CeExtKickstartImageList_Type.__name__=_Y
_CeExtKickstartImageList_Object=MibTableColumn
ceExtKickstartImageList=_CeExtKickstartImageList_Object((1,3,6,1,4,1,9,9,195,1,2,1,4),_CeExtKickstartImageList_Type())
ceExtKickstartImageList.setMaxAccess(_L)
if mibBuilder.loadTexts:ceExtKickstartImageList.setStatus(_B)
_CeExtEntityLEDTable_Object=MibTable
ceExtEntityLEDTable=_CeExtEntityLEDTable_Object((1,3,6,1,4,1,9,9,195,1,3))
if mibBuilder.loadTexts:ceExtEntityLEDTable.setStatus(_B)
_CeExtEntityLEDEntry_Object=MibTableRow
ceExtEntityLEDEntry=_CeExtEntityLEDEntry_Object((1,3,6,1,4,1,9,9,195,1,3,1))
ceExtEntityLEDEntry.setIndexNames((0,_C,_Q),(0,_A,_b))
if mibBuilder.loadTexts:ceExtEntityLEDEntry.setStatus(_B)
class _CeExtEntityLEDType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('status',1),('system',2),('active',3),('power',4),('battery',5)))
_CeExtEntityLEDType_Type.__name__=_X
_CeExtEntityLEDType_Object=MibTableColumn
ceExtEntityLEDType=_CeExtEntityLEDType_Object((1,3,6,1,4,1,9,9,195,1,3,1,1),_CeExtEntityLEDType_Type())
ceExtEntityLEDType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ceExtEntityLEDType.setStatus(_B)
class _CeExtEntityLEDColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('green',2),('amber',3),('red',4)))
_CeExtEntityLEDColor_Type.__name__=_X
_CeExtEntityLEDColor_Object=MibTableColumn
ceExtEntityLEDColor=_CeExtEntityLEDColor_Object((1,3,6,1,4,1,9,9,195,1,3,1,2),_CeExtEntityLEDColor_Type())
ceExtEntityLEDColor.setMaxAccess(_D)
if mibBuilder.loadTexts:ceExtEntityLEDColor.setStatus(_B)
_CeExtEntPhysicalTable_Object=MibTable
ceExtEntPhysicalTable=_CeExtEntPhysicalTable_Object((1,3,6,1,4,1,9,9,195,1,4))
if mibBuilder.loadTexts:ceExtEntPhysicalTable.setStatus(_B)
_CeExtEntPhysicalEntry_Object=MibTableRow
ceExtEntPhysicalEntry=_CeExtEntPhysicalEntry_Object((1,3,6,1,4,1,9,9,195,1,4,1))
if mibBuilder.loadTexts:ceExtEntPhysicalEntry.setStatus(_B)
class _CeEntPhysicalSecondSerialNum_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CeEntPhysicalSecondSerialNum_Type.__name__=_K
_CeEntPhysicalSecondSerialNum_Object=MibTableColumn
ceEntPhysicalSecondSerialNum=_CeEntPhysicalSecondSerialNum_Object((1,3,6,1,4,1,9,9,195,1,4,1,1),_CeEntPhysicalSecondSerialNum_Type())
ceEntPhysicalSecondSerialNum.setMaxAccess(_L)
if mibBuilder.loadTexts:ceEntPhysicalSecondSerialNum.setStatus(_B)
_CeExtNotificationControlObjects_ObjectIdentity=ObjectIdentity
ceExtNotificationControlObjects=_CeExtNotificationControlObjects_ObjectIdentity((1,3,6,1,4,1,9,9,195,1,5))
class _CeExtEntDoorNotifEnable_Type(TruthValue):defaultValue=2
_CeExtEntDoorNotifEnable_Type.__name__=_U
_CeExtEntDoorNotifEnable_Object=MibScalar
ceExtEntDoorNotifEnable=_CeExtEntDoorNotifEnable_Object((1,3,6,1,4,1,9,9,195,1,5,1),_CeExtEntDoorNotifEnable_Type())
ceExtEntDoorNotifEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:ceExtEntDoorNotifEnable.setStatus(_B)
class _CeExtEntBreakOutPortNotifEnable_Type(TruthValue):defaultValue=2
_CeExtEntBreakOutPortNotifEnable_Type.__name__=_U
_CeExtEntBreakOutPortNotifEnable_Object=MibScalar
ceExtEntBreakOutPortNotifEnable=_CeExtEntBreakOutPortNotifEnable_Object((1,3,6,1,4,1,9,9,195,1,5,2),_CeExtEntBreakOutPortNotifEnable_Type())
ceExtEntBreakOutPortNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ceExtEntBreakOutPortNotifEnable.setStatus(_B)
class _CeExtEntUsbModemNotifEnable_Type(TruthValue):defaultValue=2
_CeExtEntUsbModemNotifEnable_Type.__name__=_U
_CeExtEntUsbModemNotifEnable_Object=MibScalar
ceExtEntUsbModemNotifEnable=_CeExtEntUsbModemNotifEnable_Object((1,3,6,1,4,1,9,9,195,1,5,3),_CeExtEntUsbModemNotifEnable_Type())
ceExtEntUsbModemNotifEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:ceExtEntUsbModemNotifEnable.setStatus(_B)
_CeExtUSBModemTable_Object=MibTable
ceExtUSBModemTable=_CeExtUSBModemTable_Object((1,3,6,1,4,1,9,9,195,1,6))
if mibBuilder.loadTexts:ceExtUSBModemTable.setStatus(_B)
_CeExtUSBModemEntry_Object=MibTableRow
ceExtUSBModemEntry=_CeExtUSBModemEntry_Object((1,3,6,1,4,1,9,9,195,1,6,1))
ceExtUSBModemEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:ceExtUSBModemEntry.setStatus(_B)
class _CeExtUSBModemIMEI_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CeExtUSBModemIMEI_Type.__name__=_K
_CeExtUSBModemIMEI_Object=MibTableColumn
ceExtUSBModemIMEI=_CeExtUSBModemIMEI_Object((1,3,6,1,4,1,9,9,195,1,6,1,1),_CeExtUSBModemIMEI_Type())
ceExtUSBModemIMEI.setMaxAccess(_D)
if mibBuilder.loadTexts:ceExtUSBModemIMEI.setStatus(_B)
class _CeExtUSBModemIMSI_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CeExtUSBModemIMSI_Type.__name__=_K
_CeExtUSBModemIMSI_Object=MibTableColumn
ceExtUSBModemIMSI=_CeExtUSBModemIMSI_Object((1,3,6,1,4,1,9,9,195,1,6,1,2),_CeExtUSBModemIMSI_Type())
ceExtUSBModemIMSI.setMaxAccess(_D)
if mibBuilder.loadTexts:ceExtUSBModemIMSI.setStatus(_B)
class _CeExtUSBModemServiceProvider_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CeExtUSBModemServiceProvider_Type.__name__=_K
_CeExtUSBModemServiceProvider_Object=MibTableColumn
ceExtUSBModemServiceProvider=_CeExtUSBModemServiceProvider_Object((1,3,6,1,4,1,9,9,195,1,6,1,3),_CeExtUSBModemServiceProvider_Type())
ceExtUSBModemServiceProvider.setMaxAccess(_D)
if mibBuilder.loadTexts:ceExtUSBModemServiceProvider.setStatus(_B)
class _CeExtUSBModemSignalStrength_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CeExtUSBModemSignalStrength_Type.__name__=_K
_CeExtUSBModemSignalStrength_Object=MibTableColumn
ceExtUSBModemSignalStrength=_CeExtUSBModemSignalStrength_Object((1,3,6,1,4,1,9,9,195,1,6,1,4),_CeExtUSBModemSignalStrength_Type())
ceExtUSBModemSignalStrength.setMaxAccess(_D)
if mibBuilder.loadTexts:ceExtUSBModemSignalStrength.setStatus(_B)
_CeExtMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ceExtMIBNotificationPrefix=_CeExtMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,195,2))
_CiscoEntityExtMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoEntityExtMIBNotifications=_CiscoEntityExtMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,195,2,0))
_CiscoEntityExtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoEntityExtMIBConformance=_CiscoEntityExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,195,3))
_CiscoEntityExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoEntityExtMIBCompliances=_CiscoEntityExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,195,3,1))
_CiscoEntityExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoEntityExtMIBGroups=_CiscoEntityExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,195,3,2))
entPhysicalEntry.registerAugmentions((_A,_c))
ceExtEntPhysicalEntry.setIndexNames(*entPhysicalEntry.getIndexNames())
ceExtPhysicalProcessorGroup=ObjectGroup((1,3,6,1,4,1,9,9,195,3,2,1))
ceExtPhysicalProcessorGroup.setObjects(*((_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:ceExtPhysicalProcessorGroup.setStatus(_B)
ciscoEntityExtConfigRegGroup=ObjectGroup((1,3,6,1,4,1,9,9,195,3,2,2))
ciscoEntityExtConfigRegGroup.setObjects(*((_A,_g),(_A,_h)))
if mibBuilder.loadTexts:ciscoEntityExtConfigRegGroup.setStatus(_B)
ceExtSysBootImageListGroup=ObjectGroup((1,3,6,1,4,1,9,9,195,3,2,3))
ceExtSysBootImageListGroup.setObjects((_A,_i))
if mibBuilder.loadTexts:ceExtSysBootImageListGroup.setStatus(_B)
ciscoEntityExtLEDGroup=ObjectGroup((1,3,6,1,4,1,9,9,195,3,2,4))
ciscoEntityExtLEDGroup.setObjects((_A,_j))
if mibBuilder.loadTexts:ciscoEntityExtLEDGroup.setStatus(_B)
ceExtSysBootImageListGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,195,3,2,5))
ceExtSysBootImageListGroupRev1.setObjects((_A,_k))
if mibBuilder.loadTexts:ceExtSysBootImageListGroupRev1.setStatus(_B)
ciscoExtEntityPhysicalGroup=ObjectGroup((1,3,6,1,4,1,9,9,195,3,2,6))
ciscoExtEntityPhysicalGroup.setObjects((_A,_l))
if mibBuilder.loadTexts:ciscoExtEntityPhysicalGroup.setStatus(_B)
ceExtPhyProcessorOverflowGroup=ObjectGroup((1,3,6,1,4,1,9,9,195,3,2,7))
ceExtPhyProcessorOverflowGroup.setObjects((_A,_m))
if mibBuilder.loadTexts:ceExtPhyProcessorOverflowGroup.setStatus(_B)
ceExtPhyProcessorHCGroup=ObjectGroup((1,3,6,1,4,1,9,9,195,3,2,8))
ceExtPhyProcessorHCGroup.setObjects((_A,_n))
if mibBuilder.loadTexts:ceExtPhyProcessorHCGroup.setStatus(_B)
ceExtEntDoorNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,195,3,2,10))
ceExtEntDoorNotifControlGroup.setObjects((_A,_o))
if mibBuilder.loadTexts:ceExtEntDoorNotifControlGroup.setStatus(_B)
ceExtBreakOutPortNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,195,3,2,12))
ceExtBreakOutPortNotifControlGroup.setObjects((_A,_p))
if mibBuilder.loadTexts:ceExtBreakOutPortNotifControlGroup.setStatus(_B)
ceExtUSBModemGroup=ObjectGroup((1,3,6,1,4,1,9,9,195,3,2,13))
ceExtUSBModemGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:ceExtUSBModemGroup.setStatus(_B)
ceExtUsbModemNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,195,3,2,15))
ceExtUsbModemNotifControlGroup.setObjects((_A,_u))
if mibBuilder.loadTexts:ceExtUsbModemNotifControlGroup.setStatus(_B)
ceExtNVRAMOverflowGroup=ObjectGroup((1,3,6,1,4,1,9,9,195,3,2,16))
ceExtNVRAMOverflowGroup.setObjects(*((_A,_v),(_A,_w)))
if mibBuilder.loadTexts:ceExtNVRAMOverflowGroup.setStatus(_B)
ceExtHCNVRAMGroup=ObjectGroup((1,3,6,1,4,1,9,9,195,3,2,17))
ceExtHCNVRAMGroup.setObjects(*((_A,_x),(_A,_y)))
if mibBuilder.loadTexts:ceExtHCNVRAMGroup.setStatus(_B)
ceExtEntDoorCloseNotif=NotificationType((1,3,6,1,4,1,9,9,195,2,0,1))
ceExtEntDoorCloseNotif.setObjects(*((_C,_P),(_C,_R)))
if mibBuilder.loadTexts:ceExtEntDoorCloseNotif.setStatus(_B)
ceExtEntDoorOpenNotif=NotificationType((1,3,6,1,4,1,9,9,195,2,0,2))
ceExtEntDoorOpenNotif.setObjects(*((_C,_P),(_C,_R)))
if mibBuilder.loadTexts:ceExtEntDoorOpenNotif.setStatus(_B)
ceExtBreakOutPortInserted=NotificationType((1,3,6,1,4,1,9,9,195,2,0,3))
ceExtBreakOutPortInserted.setObjects(*((_C,_O),(_C,_R)))
if mibBuilder.loadTexts:ceExtBreakOutPortInserted.setStatus(_B)
ceExtBreakOutPortRemoved=NotificationType((1,3,6,1,4,1,9,9,195,2,0,4))
ceExtBreakOutPortRemoved.setObjects(*((_C,_O),(_C,_R)))
if mibBuilder.loadTexts:ceExtBreakOutPortRemoved.setStatus(_B)
ceExtUSBModemPlugInNotif=NotificationType((1,3,6,1,4,1,9,9,195,2,0,5))
ceExtUSBModemPlugInNotif.setObjects(*((_C,_O),(_C,_P)))
if mibBuilder.loadTexts:ceExtUSBModemPlugInNotif.setStatus(_B)
ceExtUSBModemPlugOutNotif=NotificationType((1,3,6,1,4,1,9,9,195,2,0,6))
ceExtUSBModemPlugOutNotif.setObjects(*((_C,_O),(_C,_P)))
if mibBuilder.loadTexts:ceExtUSBModemPlugOutNotif.setStatus(_B)
ceExtEntDoorNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,195,3,2,9))
ceExtEntDoorNotifGroup.setObjects(*((_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:ceExtEntDoorNotifGroup.setStatus(_B)
ceExtBreakOutPortNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,195,3,2,11))
ceExtBreakOutPortNotifGroup.setObjects(*((_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:ceExtBreakOutPortNotifGroup.setStatus(_B)
ceExtUsbModemNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,195,3,2,14))
ceExtUsbModemNotificationsGroup.setObjects(*((_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:ceExtUsbModemNotificationsGroup.setStatus(_B)
ciscoEntityExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,195,3,1,1))
ciscoEntityExtMIBCompliance.setObjects(*((_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ciscoEntityExtMIBCompliance.setStatus(_M)
ciscoEntityExtMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,195,3,1,2))
ciscoEntityExtMIBComplianceRev1.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:ciscoEntityExtMIBComplianceRev1.setStatus(_M)
ciscoEntityExtMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,195,3,1,3))
ciscoEntityExtMIBComplianceRev2.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_N)))
if mibBuilder.loadTexts:ciscoEntityExtMIBComplianceRev2.setStatus(_M)
ciscoEntityExtMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,195,3,1,4))
ciscoEntityExtMIBComplianceRev3.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_N),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ciscoEntityExtMIBComplianceRev3.setStatus(_M)
ciscoEntityExtMIBComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,9,195,3,1,5))
ciscoEntityExtMIBComplianceRev4.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_N),(_A,_S),(_A,_T),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:ciscoEntityExtMIBComplianceRev4.setStatus(_M)
ciscoEntityExtMIBComplianceRev5=ModuleCompliance((1,3,6,1,4,1,9,9,195,3,1,6))
ciscoEntityExtMIBComplianceRev5.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_N),(_A,_S),(_A,_T),(_A,_V),(_A,_W),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:ciscoEntityExtMIBComplianceRev5.setStatus(_M)
ciscoEntityExtMIBComplianceRev6=ModuleCompliance((1,3,6,1,4,1,9,9,195,3,1,7))
ciscoEntityExtMIBComplianceRev6.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_N),(_A,_S),(_A,_T),(_A,_V),(_A,_W),(_A,_Z),(_A,_a),(_A,_A5),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:ciscoEntityExtMIBComplianceRev6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ConfigRegisterValue':ConfigRegisterValue,_Y:BootImageList,'ciscoEntityExtMIB':ciscoEntityExtMIB,'ciscoEntityExtMIBObjects':ciscoEntityExtMIBObjects,'ceExtPhysicalProcessorTable':ceExtPhysicalProcessorTable,'ceExtPhysicalProcessorEntry':ceExtPhysicalProcessorEntry,_d:ceExtProcessorRam,_e:ceExtNVRAMSize,_f:ceExtNVRAMUsed,_m:ceExtProcessorRamOverflow,_n:ceExtHCProcessorRam,_v:ceExtNVRAMSizeOverflow,_x:ceExtHCNVRAMSize,_w:ceExtNVRAMUsedOverflow,_y:ceExtHCNVRAMUsed,'ceExtConfigRegTable':ceExtConfigRegTable,'ceExtConfigRegEntry':ceExtConfigRegEntry,_g:ceExtConfigRegister,_h:ceExtConfigRegNext,_i:ceExtSysBootImageList,_k:ceExtKickstartImageList,'ceExtEntityLEDTable':ceExtEntityLEDTable,'ceExtEntityLEDEntry':ceExtEntityLEDEntry,_b:ceExtEntityLEDType,_j:ceExtEntityLEDColor,'ceExtEntPhysicalTable':ceExtEntPhysicalTable,_c:ceExtEntPhysicalEntry,_l:ceEntPhysicalSecondSerialNum,'ceExtNotificationControlObjects':ceExtNotificationControlObjects,_o:ceExtEntDoorNotifEnable,_p:ceExtEntBreakOutPortNotifEnable,_u:ceExtEntUsbModemNotifEnable,'ceExtUSBModemTable':ceExtUSBModemTable,'ceExtUSBModemEntry':ceExtUSBModemEntry,_q:ceExtUSBModemIMEI,_r:ceExtUSBModemIMSI,_s:ceExtUSBModemServiceProvider,_t:ceExtUSBModemSignalStrength,'ceExtMIBNotificationPrefix':ceExtMIBNotificationPrefix,'ciscoEntityExtMIBNotifications':ciscoEntityExtMIBNotifications,_z:ceExtEntDoorCloseNotif,_A0:ceExtEntDoorOpenNotif,_A1:ceExtBreakOutPortInserted,_A2:ceExtBreakOutPortRemoved,_A3:ceExtUSBModemPlugInNotif,_A4:ceExtUSBModemPlugOutNotif,'ciscoEntityExtMIBConformance':ciscoEntityExtMIBConformance,'ciscoEntityExtMIBCompliances':ciscoEntityExtMIBCompliances,'ciscoEntityExtMIBCompliance':ciscoEntityExtMIBCompliance,'ciscoEntityExtMIBComplianceRev1':ciscoEntityExtMIBComplianceRev1,'ciscoEntityExtMIBComplianceRev2':ciscoEntityExtMIBComplianceRev2,'ciscoEntityExtMIBComplianceRev3':ciscoEntityExtMIBComplianceRev3,'ciscoEntityExtMIBComplianceRev4':ciscoEntityExtMIBComplianceRev4,'ciscoEntityExtMIBComplianceRev5':ciscoEntityExtMIBComplianceRev5,'ciscoEntityExtMIBComplianceRev6':ciscoEntityExtMIBComplianceRev6,'ciscoEntityExtMIBGroups':ciscoEntityExtMIBGroups,_F:ceExtPhysicalProcessorGroup,_G:ciscoEntityExtConfigRegGroup,_H:ceExtSysBootImageListGroup,_I:ciscoEntityExtLEDGroup,_J:ceExtSysBootImageListGroupRev1,_N:ciscoExtEntityPhysicalGroup,_S:ceExtPhyProcessorOverflowGroup,_T:ceExtPhyProcessorHCGroup,_V:ceExtEntDoorNotifGroup,_W:ceExtEntDoorNotifControlGroup,_Z:ceExtBreakOutPortNotifGroup,_a:ceExtBreakOutPortNotifControlGroup,_A5:ceExtUSBModemGroup,_A6:ceExtUsbModemNotificationsGroup,_A7:ceExtUsbModemNotifControlGroup,'ceExtNVRAMOverflowGroup':ceExtNVRAMOverflowGroup,'ceExtHCNVRAMGroup':ceExtHCNVRAMGroup})