_K='Integer32'
_J='sysName'
_I='SNMPv2-MIB'
_H='adTAeSCUTrapAlarmLevel'
_G='ADTRAN-TAeSCUEXT1-MIB'
_F='adTrapInformSeqNum'
_E='ADTRAN-GENTRAPINFORM-MIB'
_D='adGenSlotProdName'
_C='adGenSlotInfoIndex'
_B='current'
_A='ADTRAN-GENSLOT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,adGenSlotProdName=mibBuilder.importSymbols(_A,_C,_D)
adTrapInformSeqNum,=mibBuilder.importSymbols(_E,_F)
adMgmt,adProducts=mibBuilder.importSymbols('ADTRAN-MIB','adMgmt','adProducts')
adTAeSCUTrapAlarmLevel,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_I,_J)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adTA1100Fcfmg=ModuleIdentity((1,3,6,1,4,1,664,2,827))
if mibBuilder.loadTexts:adTA1100Fcfmg.setRevisions(('2010-02-24 13:00',))
_AdTA1100Fff_ObjectIdentity=ObjectIdentity
adTA1100Fff=_AdTA1100Fff_ObjectIdentity((1,3,6,1,4,1,664,1,824))
_AdTA1100FffScm_ObjectIdentity=ObjectIdentity
adTA1100FffScm=_AdTA1100FffScm_ObjectIdentity((1,3,6,1,4,1,664,1,825))
_AdTA1100Fcf_ObjectIdentity=ObjectIdentity
adTA1100Fcf=_AdTA1100Fcf_ObjectIdentity((1,3,6,1,4,1,664,1,827))
_AdTA1100FcfSCMNotificationEvents_ObjectIdentity=ObjectIdentity
adTA1100FcfSCMNotificationEvents=_AdTA1100FcfSCMNotificationEvents_ObjectIdentity((1,3,6,1,4,1,664,1,827,0))
if mibBuilder.loadTexts:adTA1100FcfSCMNotificationEvents.setStatus(_B)
_AdTA1100FcfScm_ObjectIdentity=ObjectIdentity
adTA1100FcfScm=_AdTA1100FcfScm_ObjectIdentity((1,3,6,1,4,1,664,1,828))
_AdTA1248EthIP_ObjectIdentity=ObjectIdentity
adTA1248EthIP=_AdTA1248EthIP_ObjectIdentity((1,3,6,1,4,1,664,1,867))
_AdTA1200Fff_ObjectIdentity=ObjectIdentity
adTA1200Fff=_AdTA1200Fff_ObjectIdentity((1,3,6,1,4,1,664,1,883))
_AdTA1200FffScm_ObjectIdentity=ObjectIdentity
adTA1200FffScm=_AdTA1200FffScm_ObjectIdentity((1,3,6,1,4,1,664,1,884))
_AdTA1248EthIPScm_ObjectIdentity=ObjectIdentity
adTA1248EthIPScm=_AdTA1248EthIPScm_ObjectIdentity((1,3,6,1,4,1,664,1,886))
_AdTA1124PT1_ObjectIdentity=ObjectIdentity
adTA1124PT1=_AdTA1124PT1_ObjectIdentity((1,3,6,1,4,1,664,1,958))
_AdTA1124PT1Scm_ObjectIdentity=ObjectIdentity
adTA1124PT1Scm=_AdTA1124PT1Scm_ObjectIdentity((1,3,6,1,4,1,664,1,959))
_AdTA1124PHDSL4_ObjectIdentity=ObjectIdentity
adTA1124PHDSL4=_AdTA1124PHDSL4_ObjectIdentity((1,3,6,1,4,1,664,1,962))
_AdTA1100Fffmg_ObjectIdentity=ObjectIdentity
adTA1100Fffmg=_AdTA1100Fffmg_ObjectIdentity((1,3,6,1,4,1,664,2,824))
_AdTA1100FSysConfig_ObjectIdentity=ObjectIdentity
adTA1100FSysConfig=_AdTA1100FSysConfig_ObjectIdentity((1,3,6,1,4,1,664,2,827,10))
class _AdTATIDSysNameSyncEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AdTATIDSysNameSyncEnable_Type.__name__=_K
_AdTATIDSysNameSyncEnable_Object=MibScalar
adTATIDSysNameSyncEnable=_AdTATIDSysNameSyncEnable_Object((1,3,6,1,4,1,664,2,827,10,1),_AdTATIDSysNameSyncEnable_Type())
adTATIDSysNameSyncEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:adTATIDSysNameSyncEnable.setStatus(_B)
adTADeviceMgmtRestored=NotificationType((1,3,6,1,4,1,664,1,827,0,82402))
adTADeviceMgmtRestored.setObjects(*((_E,_F),(_I,_J),(_A,_C),(_G,_H),(_A,_D)))
if mibBuilder.loadTexts:adTADeviceMgmtRestored.setStatus(_B)
adTADeviceMgmtFail=NotificationType((1,3,6,1,4,1,664,1,827,0,82403))
adTADeviceMgmtFail.setObjects(*((_E,_F),(_I,_J),(_A,_C),(_G,_H),(_A,_D)))
if mibBuilder.loadTexts:adTADeviceMgmtFail.setStatus(_B)
adTADeviceInserted=NotificationType((1,3,6,1,4,1,664,1,827,0,82404))
adTADeviceInserted.setObjects(*((_E,_F),(_I,_J),(_A,_C),(_G,_H),(_A,_D)))
if mibBuilder.loadTexts:adTADeviceInserted.setStatus(_B)
adTADeviceRemoved=NotificationType((1,3,6,1,4,1,664,1,827,0,82405))
adTADeviceRemoved.setObjects(*((_E,_F),(_I,_J),(_A,_C),(_G,_H),(_A,_D)))
if mibBuilder.loadTexts:adTADeviceRemoved.setStatus(_B)
mibBuilder.exportSymbols('ADTRAN-TA1100FSCM-MIB',**{'adTA1100Fff':adTA1100Fff,'adTA1100FffScm':adTA1100FffScm,'adTA1100Fcf':adTA1100Fcf,'adTA1100FcfSCMNotificationEvents':adTA1100FcfSCMNotificationEvents,'adTADeviceMgmtRestored':adTADeviceMgmtRestored,'adTADeviceMgmtFail':adTADeviceMgmtFail,'adTADeviceInserted':adTADeviceInserted,'adTADeviceRemoved':adTADeviceRemoved,'adTA1100FcfScm':adTA1100FcfScm,'adTA1248EthIP':adTA1248EthIP,'adTA1200Fff':adTA1200Fff,'adTA1200FffScm':adTA1200FffScm,'adTA1248EthIPScm':adTA1248EthIPScm,'adTA1124PT1':adTA1124PT1,'adTA1124PT1Scm':adTA1124PT1Scm,'adTA1124PHDSL4':adTA1124PHDSL4,'adTA1100Fffmg':adTA1100Fffmg,'adTA1100Fcfmg':adTA1100Fcfmg,'adTA1100FSysConfig':adTA1100FSysConfig,'adTATIDSysNameSyncEnable':adTATIDSysNameSyncEnable})