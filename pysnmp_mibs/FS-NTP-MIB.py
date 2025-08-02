_W='fsNtpMIBGroups'
_V='fsNtpServerStatus'
_U='fsNtpServerVersion'
_T='fsTimeSyncPeriod'
_S='fsTimeAfterNTPCal'
_R='fsNTPServerIPAdd'
_Q='fsntpSysRefTime'
_P='fsntpSysRefId'
_O='fsntpSysRootDispersion'
_N='fsntpSysRootDelay'
_M='fsntpSysPrecision'
_L='fsntpSysStratum'
_K='fsntpSysLeap'
_J='read-create'
_I='OctetString'
_H='fsntpSysState'
_G='fsNtpServerNetAddr'
_F='fsNtpServerNetType'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='FS-NTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fsNtpMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,49))
if mibBuilder.loadTexts:fsNtpMIB.setRevisions(('2009-05-14 00:00',))
class NTPTimeStamp(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class NTPLeapIndicator(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noWarning',0),('addSecond',1),('subtractSecond',2),('alarm',3)))
class NTPSignedTimeValue(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class NTPUnsignedTimeValue(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class NTPStratum(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class NTPRefId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_FsNtpMIBObjects_ObjectIdentity=ObjectIdentity
fsNtpMIBObjects=_FsNtpMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,49,1))
_FsntpSystem_ObjectIdentity=ObjectIdentity
fsntpSystem=_FsntpSystem_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,49,1,1))
_FsntpSysLeap_Type=NTPLeapIndicator
_FsntpSysLeap_Object=MibScalar
fsntpSysLeap=_FsntpSysLeap_Object((1,3,6,1,4,1,52642,1,1,10,2,49,1,1,1),_FsntpSysLeap_Type())
fsntpSysLeap.setMaxAccess(_E)
if mibBuilder.loadTexts:fsntpSysLeap.setStatus(_A)
_FsntpSysStratum_Type=NTPStratum
_FsntpSysStratum_Object=MibScalar
fsntpSysStratum=_FsntpSysStratum_Object((1,3,6,1,4,1,52642,1,1,10,2,49,1,1,2),_FsntpSysStratum_Type())
fsntpSysStratum.setMaxAccess(_E)
if mibBuilder.loadTexts:fsntpSysStratum.setStatus(_A)
class _FsntpSysPrecision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-24,24))
_FsntpSysPrecision_Type.__name__=_D
_FsntpSysPrecision_Object=MibScalar
fsntpSysPrecision=_FsntpSysPrecision_Object((1,3,6,1,4,1,52642,1,1,10,2,49,1,1,3),_FsntpSysPrecision_Type())
fsntpSysPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:fsntpSysPrecision.setStatus(_A)
_FsntpSysRootDelay_Type=NTPSignedTimeValue
_FsntpSysRootDelay_Object=MibScalar
fsntpSysRootDelay=_FsntpSysRootDelay_Object((1,3,6,1,4,1,52642,1,1,10,2,49,1,1,4),_FsntpSysRootDelay_Type())
fsntpSysRootDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:fsntpSysRootDelay.setStatus(_A)
_FsntpSysRootDispersion_Type=NTPUnsignedTimeValue
_FsntpSysRootDispersion_Object=MibScalar
fsntpSysRootDispersion=_FsntpSysRootDispersion_Object((1,3,6,1,4,1,52642,1,1,10,2,49,1,1,5),_FsntpSysRootDispersion_Type())
fsntpSysRootDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fsntpSysRootDispersion.setStatus(_A)
_FsntpSysRefId_Type=NTPRefId
_FsntpSysRefId_Object=MibScalar
fsntpSysRefId=_FsntpSysRefId_Object((1,3,6,1,4,1,52642,1,1,10,2,49,1,1,6),_FsntpSysRefId_Type())
fsntpSysRefId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsntpSysRefId.setStatus(_A)
_FsntpSysRefTime_Type=NTPTimeStamp
_FsntpSysRefTime_Object=MibScalar
fsntpSysRefTime=_FsntpSysRefTime_Object((1,3,6,1,4,1,52642,1,1,10,2,49,1,1,7),_FsntpSysRefTime_Type())
fsntpSysRefTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsntpSysRefTime.setStatus(_A)
_FsNTPServerIPAdd_Type=IpAddress
_FsNTPServerIPAdd_Object=MibScalar
fsNTPServerIPAdd=_FsNTPServerIPAdd_Object((1,3,6,1,4,1,52642,1,1,10,2,49,1,1,8),_FsNTPServerIPAdd_Type())
fsNTPServerIPAdd.setMaxAccess(_E)
if mibBuilder.loadTexts:fsNTPServerIPAdd.setStatus(_A)
class _FsTimeAfterNTPCal_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_FsTimeAfterNTPCal_Type.__name__=_I
_FsTimeAfterNTPCal_Object=MibScalar
fsTimeAfterNTPCal=_FsTimeAfterNTPCal_Object((1,3,6,1,4,1,52642,1,1,10,2,49,1,1,9),_FsTimeAfterNTPCal_Type())
fsTimeAfterNTPCal.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTimeAfterNTPCal.setStatus(_A)
class _FsTimeSyncPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8640000))
_FsTimeSyncPeriod_Type.__name__=_D
_FsTimeSyncPeriod_Object=MibScalar
fsTimeSyncPeriod=_FsTimeSyncPeriod_Object((1,3,6,1,4,1,52642,1,1,10,2,49,1,1,10),_FsTimeSyncPeriod_Type())
fsTimeSyncPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:fsTimeSyncPeriod.setStatus(_A)
_FsNtpServerTable_Object=MibTable
fsNtpServerTable=_FsNtpServerTable_Object((1,3,6,1,4,1,52642,1,1,10,2,49,1,1,11))
if mibBuilder.loadTexts:fsNtpServerTable.setStatus(_A)
_FsNtpServerEntry_Object=MibTableRow
fsNtpServerEntry=_FsNtpServerEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,49,1,1,11,1))
fsNtpServerEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:fsNtpServerEntry.setStatus(_A)
_FsNtpServerNetType_Type=InetAddressType
_FsNtpServerNetType_Object=MibTableColumn
fsNtpServerNetType=_FsNtpServerNetType_Object((1,3,6,1,4,1,52642,1,1,10,2,49,1,1,11,1,1),_FsNtpServerNetType_Type())
fsNtpServerNetType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNtpServerNetType.setStatus(_A)
_FsNtpServerNetAddr_Type=InetAddress
_FsNtpServerNetAddr_Object=MibTableColumn
fsNtpServerNetAddr=_FsNtpServerNetAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,49,1,1,11,1,2),_FsNtpServerNetAddr_Type())
fsNtpServerNetAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNtpServerNetAddr.setStatus(_A)
class _FsNtpServerVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('version1',1),('version2',2),('version3',3)))
_FsNtpServerVersion_Type.__name__=_D
_FsNtpServerVersion_Object=MibTableColumn
fsNtpServerVersion=_FsNtpServerVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,49,1,1,11,1,3),_FsNtpServerVersion_Type())
fsNtpServerVersion.setMaxAccess(_J)
if mibBuilder.loadTexts:fsNtpServerVersion.setStatus(_A)
_FsNtpServerStatus_Type=RowStatus
_FsNtpServerStatus_Object=MibTableColumn
fsNtpServerStatus=_FsNtpServerStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,49,1,1,11,1,4),_FsNtpServerStatus_Type())
fsNtpServerStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:fsNtpServerStatus.setStatus(_A)
class _FsntpSysState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unsynchronized',0),('synchronized',1)))
_FsntpSysState_Type.__name__=_D
_FsntpSysState_Object=MibScalar
fsntpSysState=_FsntpSysState_Object((1,3,6,1,4,1,52642,1,1,10,2,49,1,1,12),_FsntpSysState_Type())
fsntpSysState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsntpSysState.setStatus(_A)
_FsNtpMIBTrap_ObjectIdentity=ObjectIdentity
fsNtpMIBTrap=_FsNtpMIBTrap_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,49,1,2))
_FsNtpMIBConformance_ObjectIdentity=ObjectIdentity
fsNtpMIBConformance=_FsNtpMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,49,2))
_FsNtpMIBCompliances_ObjectIdentity=ObjectIdentity
fsNtpMIBCompliances=_FsNtpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,49,2,1))
_FsNtpMIBGroups_ObjectIdentity=ObjectIdentity
fsNtpMIBGroups=_FsNtpMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,49,2,2))
fsNtpSysGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,49,2,2,1))
fsNtpSysGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_F),(_B,_G),(_B,_U),(_B,_V),(_B,_H)))
if mibBuilder.loadTexts:fsNtpSysGroup.setStatus(_A)
fsNtpStatussyncTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,49,1,2,1))
fsNtpStatussyncTrap.setObjects((_B,_H))
if mibBuilder.loadTexts:fsNtpStatussyncTrap.setStatus(_A)
fsNtpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,49,2,1,1))
fsNtpMIBCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:fsNtpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NTPTimeStamp':NTPTimeStamp,'NTPLeapIndicator':NTPLeapIndicator,'NTPSignedTimeValue':NTPSignedTimeValue,'NTPUnsignedTimeValue':NTPUnsignedTimeValue,'NTPStratum':NTPStratum,'NTPRefId':NTPRefId,'fsNtpMIB':fsNtpMIB,'fsNtpMIBObjects':fsNtpMIBObjects,'fsntpSystem':fsntpSystem,_K:fsntpSysLeap,_L:fsntpSysStratum,_M:fsntpSysPrecision,_N:fsntpSysRootDelay,_O:fsntpSysRootDispersion,_P:fsntpSysRefId,_Q:fsntpSysRefTime,_R:fsNTPServerIPAdd,_S:fsTimeAfterNTPCal,_T:fsTimeSyncPeriod,'fsNtpServerTable':fsNtpServerTable,'fsNtpServerEntry':fsNtpServerEntry,_F:fsNtpServerNetType,_G:fsNtpServerNetAddr,_U:fsNtpServerVersion,_V:fsNtpServerStatus,_H:fsntpSysState,'fsNtpMIBTrap':fsNtpMIBTrap,'fsNtpStatussyncTrap':fsNtpStatussyncTrap,'fsNtpMIBConformance':fsNtpMIBConformance,'fsNtpMIBCompliances':fsNtpMIBCompliances,'fsNtpMIBCompliance':fsNtpMIBCompliance,_W:fsNtpMIBGroups,'fsNtpSysGroup':fsNtpSysGroup})