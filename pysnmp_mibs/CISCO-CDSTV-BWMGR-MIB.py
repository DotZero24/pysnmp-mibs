_N='ciscoCdstvBWMgrMIBMainObjectGroup'
_M='cdstvBWMgrAddressType'
_L='cdstvBWMgrSyncAlarm'
_K='cdstvBWMgrSyncThreadPool'
_J='cdstvBWMgrServerThreadPool'
_I='cdstvBWMgrDatabaseThreadPool'
_H='cdstvBWMgrPort'
_G='cdstvBWMgrAddress'
_F='InetPortNumber'
_E='TimeIntervalSec'
_D='Unsigned32'
_C='read-write'
_B='CISCO-CDSTV-BWMGR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
TimeIntervalSec,=mibBuilder.importSymbols('CISCO-TC',_E)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoCdstvBwmgrMIB=ModuleIdentity((1,3,6,1,4,1,9,9,749))
if mibBuilder.loadTexts:ciscoCdstvBwmgrMIB.setRevisions(('2010-06-24 00:00',))
_CiscoCdstvBWMgrMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoCdstvBWMgrMIBNotifs=_CiscoCdstvBWMgrMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,749,0))
_CiscoCdstvBWMgrMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCdstvBWMgrMIBObjects=_CiscoCdstvBWMgrMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,749,1))
_CdstvBWMgrAddressType_Type=InetAddressType
_CdstvBWMgrAddressType_Object=MibScalar
cdstvBWMgrAddressType=_CdstvBWMgrAddressType_Object((1,3,6,1,4,1,9,9,749,1,1),_CdstvBWMgrAddressType_Type())
cdstvBWMgrAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvBWMgrAddressType.setStatus(_A)
_CdstvBWMgrAddress_Type=InetAddress
_CdstvBWMgrAddress_Object=MibScalar
cdstvBWMgrAddress=_CdstvBWMgrAddress_Object((1,3,6,1,4,1,9,9,749,1,2),_CdstvBWMgrAddress_Type())
cdstvBWMgrAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvBWMgrAddress.setStatus(_A)
class _CdstvBWMgrPort_Type(InetPortNumber):defaultValue=7791;subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CdstvBWMgrPort_Type.__name__=_F
_CdstvBWMgrPort_Object=MibScalar
cdstvBWMgrPort=_CdstvBWMgrPort_Object((1,3,6,1,4,1,9,9,749,1,3),_CdstvBWMgrPort_Type())
cdstvBWMgrPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvBWMgrPort.setStatus(_A)
class _CdstvBWMgrDatabaseThreadPool_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_CdstvBWMgrDatabaseThreadPool_Type.__name__=_D
_CdstvBWMgrDatabaseThreadPool_Object=MibScalar
cdstvBWMgrDatabaseThreadPool=_CdstvBWMgrDatabaseThreadPool_Object((1,3,6,1,4,1,9,9,749,1,4),_CdstvBWMgrDatabaseThreadPool_Type())
cdstvBWMgrDatabaseThreadPool.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvBWMgrDatabaseThreadPool.setStatus(_A)
class _CdstvBWMgrServerThreadPool_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_CdstvBWMgrServerThreadPool_Type.__name__=_D
_CdstvBWMgrServerThreadPool_Object=MibScalar
cdstvBWMgrServerThreadPool=_CdstvBWMgrServerThreadPool_Object((1,3,6,1,4,1,9,9,749,1,5),_CdstvBWMgrServerThreadPool_Type())
cdstvBWMgrServerThreadPool.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvBWMgrServerThreadPool.setStatus(_A)
class _CdstvBWMgrSyncThreadPool_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_CdstvBWMgrSyncThreadPool_Type.__name__=_D
_CdstvBWMgrSyncThreadPool_Object=MibScalar
cdstvBWMgrSyncThreadPool=_CdstvBWMgrSyncThreadPool_Object((1,3,6,1,4,1,9,9,749,1,6),_CdstvBWMgrSyncThreadPool_Type())
cdstvBWMgrSyncThreadPool.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvBWMgrSyncThreadPool.setStatus(_A)
class _CdstvBWMgrSyncAlarm_Type(TimeIntervalSec):defaultValue=864000;subtypeSpec=TimeIntervalSec.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2400,4294967295))
_CdstvBWMgrSyncAlarm_Type.__name__=_E
_CdstvBWMgrSyncAlarm_Object=MibScalar
cdstvBWMgrSyncAlarm=_CdstvBWMgrSyncAlarm_Object((1,3,6,1,4,1,9,9,749,1,7),_CdstvBWMgrSyncAlarm_Type())
cdstvBWMgrSyncAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvBWMgrSyncAlarm.setStatus(_A)
if mibBuilder.loadTexts:cdstvBWMgrSyncAlarm.setUnits('seconds')
_CiscoCdstvBWMgrMIBConform_ObjectIdentity=ObjectIdentity
ciscoCdstvBWMgrMIBConform=_CiscoCdstvBWMgrMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,749,2))
_CiscoCdstvBWMgrMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCdstvBWMgrMIBCompliances=_CiscoCdstvBWMgrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,749,2,1))
_CiscoCdstvBWMgrMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCdstvBWMgrMIBGroups=_CiscoCdstvBWMgrMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,749,2,2))
ciscoCdstvBWMgrMIBMainObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,749,2,2,1))
ciscoCdstvBWMgrMIBMainObjectGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ciscoCdstvBWMgrMIBMainObjectGroup.setStatus(_A)
ciscoCdstvBWMgrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,749,2,1,1))
ciscoCdstvBWMgrMIBCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:ciscoCdstvBWMgrMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCdstvBwmgrMIB':ciscoCdstvBwmgrMIB,'ciscoCdstvBWMgrMIBNotifs':ciscoCdstvBWMgrMIBNotifs,'ciscoCdstvBWMgrMIBObjects':ciscoCdstvBWMgrMIBObjects,_M:cdstvBWMgrAddressType,_G:cdstvBWMgrAddress,_H:cdstvBWMgrPort,_I:cdstvBWMgrDatabaseThreadPool,_J:cdstvBWMgrServerThreadPool,_K:cdstvBWMgrSyncThreadPool,_L:cdstvBWMgrSyncAlarm,'ciscoCdstvBWMgrMIBConform':ciscoCdstvBWMgrMIBConform,'ciscoCdstvBWMgrMIBCompliances':ciscoCdstvBWMgrMIBCompliances,'ciscoCdstvBWMgrMIBCompliance':ciscoCdstvBWMgrMIBCompliance,'ciscoCdstvBWMgrMIBGroups':ciscoCdstvBWMgrMIBGroups,_N:ciscoCdstvBWMgrMIBMainObjectGroup})