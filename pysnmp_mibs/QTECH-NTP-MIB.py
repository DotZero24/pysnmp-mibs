_V='qtechNtpMIBGroups'
_U='qtechNtpServerStatus'
_T='qtechNtpServerVersion'
_S='qtechTimeSyncPeriod'
_R='qtechTimeAfterNTPCal'
_Q='qtechNTPServerIPAdd'
_P='qtechntpSysRefTime'
_O='qtechntpSysRefId'
_N='qtechntpSysRootDispersion'
_M='qtechntpSysRootDelay'
_L='qtechntpSysPrecision'
_K='qtechntpSysStratum'
_J='qtechntpSysLeap'
_I='read-create'
_H='OctetString'
_G='qtechNtpServerNetAddr'
_F='qtechNtpServerNetType'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='QTECH-NTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
qtechNtpMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,49))
if mibBuilder.loadTexts:qtechNtpMIB.setRevisions(('2009-05-14 00:00',))
class NTPTimeStamp(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class NTPLeapIndicator(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noWarning',0),('addSecond',1),('subtractSecond',2),('alarm',3)))
class NTPSignedTimeValue(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class NTPUnsignedTimeValue(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class NTPStratum(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class NTPRefId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_QtechNtpMIBObjects_ObjectIdentity=ObjectIdentity
qtechNtpMIBObjects=_QtechNtpMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,49,1))
_QtechntpSystem_ObjectIdentity=ObjectIdentity
qtechntpSystem=_QtechntpSystem_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,49,1,1))
_QtechntpSysLeap_Type=NTPLeapIndicator
_QtechntpSysLeap_Object=MibScalar
qtechntpSysLeap=_QtechntpSysLeap_Object((1,3,6,1,4,1,27514,1,1,10,2,49,1,1,1),_QtechntpSysLeap_Type())
qtechntpSysLeap.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechntpSysLeap.setStatus(_A)
_QtechntpSysStratum_Type=NTPStratum
_QtechntpSysStratum_Object=MibScalar
qtechntpSysStratum=_QtechntpSysStratum_Object((1,3,6,1,4,1,27514,1,1,10,2,49,1,1,2),_QtechntpSysStratum_Type())
qtechntpSysStratum.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechntpSysStratum.setStatus(_A)
class _QtechntpSysPrecision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-24,24))
_QtechntpSysPrecision_Type.__name__=_D
_QtechntpSysPrecision_Object=MibScalar
qtechntpSysPrecision=_QtechntpSysPrecision_Object((1,3,6,1,4,1,27514,1,1,10,2,49,1,1,3),_QtechntpSysPrecision_Type())
qtechntpSysPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechntpSysPrecision.setStatus(_A)
_QtechntpSysRootDelay_Type=NTPSignedTimeValue
_QtechntpSysRootDelay_Object=MibScalar
qtechntpSysRootDelay=_QtechntpSysRootDelay_Object((1,3,6,1,4,1,27514,1,1,10,2,49,1,1,4),_QtechntpSysRootDelay_Type())
qtechntpSysRootDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechntpSysRootDelay.setStatus(_A)
_QtechntpSysRootDispersion_Type=NTPUnsignedTimeValue
_QtechntpSysRootDispersion_Object=MibScalar
qtechntpSysRootDispersion=_QtechntpSysRootDispersion_Object((1,3,6,1,4,1,27514,1,1,10,2,49,1,1,5),_QtechntpSysRootDispersion_Type())
qtechntpSysRootDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechntpSysRootDispersion.setStatus(_A)
_QtechntpSysRefId_Type=NTPRefId
_QtechntpSysRefId_Object=MibScalar
qtechntpSysRefId=_QtechntpSysRefId_Object((1,3,6,1,4,1,27514,1,1,10,2,49,1,1,6),_QtechntpSysRefId_Type())
qtechntpSysRefId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechntpSysRefId.setStatus(_A)
_QtechntpSysRefTime_Type=NTPTimeStamp
_QtechntpSysRefTime_Object=MibScalar
qtechntpSysRefTime=_QtechntpSysRefTime_Object((1,3,6,1,4,1,27514,1,1,10,2,49,1,1,7),_QtechntpSysRefTime_Type())
qtechntpSysRefTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechntpSysRefTime.setStatus(_A)
_QtechNTPServerIPAdd_Type=IpAddress
_QtechNTPServerIPAdd_Object=MibScalar
qtechNTPServerIPAdd=_QtechNTPServerIPAdd_Object((1,3,6,1,4,1,27514,1,1,10,2,49,1,1,8),_QtechNTPServerIPAdd_Type())
qtechNTPServerIPAdd.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechNTPServerIPAdd.setStatus(_A)
class _QtechTimeAfterNTPCal_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_QtechTimeAfterNTPCal_Type.__name__=_H
_QtechTimeAfterNTPCal_Object=MibScalar
qtechTimeAfterNTPCal=_QtechTimeAfterNTPCal_Object((1,3,6,1,4,1,27514,1,1,10,2,49,1,1,9),_QtechTimeAfterNTPCal_Type())
qtechTimeAfterNTPCal.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTimeAfterNTPCal.setStatus(_A)
class _QtechTimeSyncPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8640000))
_QtechTimeSyncPeriod_Type.__name__=_D
_QtechTimeSyncPeriod_Object=MibScalar
qtechTimeSyncPeriod=_QtechTimeSyncPeriod_Object((1,3,6,1,4,1,27514,1,1,10,2,49,1,1,10),_QtechTimeSyncPeriod_Type())
qtechTimeSyncPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechTimeSyncPeriod.setStatus(_A)
_QtechNtpServerTable_Object=MibTable
qtechNtpServerTable=_QtechNtpServerTable_Object((1,3,6,1,4,1,27514,1,1,10,2,49,1,1,11))
if mibBuilder.loadTexts:qtechNtpServerTable.setStatus(_A)
_QtechNtpServerEntry_Object=MibTableRow
qtechNtpServerEntry=_QtechNtpServerEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,49,1,1,11,1))
qtechNtpServerEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:qtechNtpServerEntry.setStatus(_A)
_QtechNtpServerNetType_Type=InetAddressType
_QtechNtpServerNetType_Object=MibTableColumn
qtechNtpServerNetType=_QtechNtpServerNetType_Object((1,3,6,1,4,1,27514,1,1,10,2,49,1,1,11,1,1),_QtechNtpServerNetType_Type())
qtechNtpServerNetType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNtpServerNetType.setStatus(_A)
_QtechNtpServerNetAddr_Type=InetAddress
_QtechNtpServerNetAddr_Object=MibTableColumn
qtechNtpServerNetAddr=_QtechNtpServerNetAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,49,1,1,11,1,2),_QtechNtpServerNetAddr_Type())
qtechNtpServerNetAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNtpServerNetAddr.setStatus(_A)
class _QtechNtpServerVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('version1',1),('version2',2),('version3',3)))
_QtechNtpServerVersion_Type.__name__=_D
_QtechNtpServerVersion_Object=MibTableColumn
qtechNtpServerVersion=_QtechNtpServerVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,49,1,1,11,1,3),_QtechNtpServerVersion_Type())
qtechNtpServerVersion.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechNtpServerVersion.setStatus(_A)
_QtechNtpServerStatus_Type=RowStatus
_QtechNtpServerStatus_Object=MibTableColumn
qtechNtpServerStatus=_QtechNtpServerStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,49,1,1,11,1,4),_QtechNtpServerStatus_Type())
qtechNtpServerStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechNtpServerStatus.setStatus(_A)
_QtechNtpMIBConformance_ObjectIdentity=ObjectIdentity
qtechNtpMIBConformance=_QtechNtpMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,49,2))
_QtechNtpMIBCompliances_ObjectIdentity=ObjectIdentity
qtechNtpMIBCompliances=_QtechNtpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,49,2,1))
_QtechNtpMIBGroups_ObjectIdentity=ObjectIdentity
qtechNtpMIBGroups=_QtechNtpMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,49,2,2))
qtechNtpSysGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,49,2,2,1))
qtechNtpSysGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_F),(_B,_G),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:qtechNtpSysGroup.setStatus(_A)
qtechNtpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,49,2,1,1))
qtechNtpMIBCompliance.setObjects((_B,_V))
if mibBuilder.loadTexts:qtechNtpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NTPTimeStamp':NTPTimeStamp,'NTPLeapIndicator':NTPLeapIndicator,'NTPSignedTimeValue':NTPSignedTimeValue,'NTPUnsignedTimeValue':NTPUnsignedTimeValue,'NTPStratum':NTPStratum,'NTPRefId':NTPRefId,'qtechNtpMIB':qtechNtpMIB,'qtechNtpMIBObjects':qtechNtpMIBObjects,'qtechntpSystem':qtechntpSystem,_J:qtechntpSysLeap,_K:qtechntpSysStratum,_L:qtechntpSysPrecision,_M:qtechntpSysRootDelay,_N:qtechntpSysRootDispersion,_O:qtechntpSysRefId,_P:qtechntpSysRefTime,_Q:qtechNTPServerIPAdd,_R:qtechTimeAfterNTPCal,_S:qtechTimeSyncPeriod,'qtechNtpServerTable':qtechNtpServerTable,'qtechNtpServerEntry':qtechNtpServerEntry,_F:qtechNtpServerNetType,_G:qtechNtpServerNetAddr,_T:qtechNtpServerVersion,_U:qtechNtpServerStatus,'qtechNtpMIBConformance':qtechNtpMIBConformance,'qtechNtpMIBCompliances':qtechNtpMIBCompliances,'qtechNtpMIBCompliance':qtechNtpMIBCompliance,_V:qtechNtpMIBGroups,'qtechNtpSysGroup':qtechNtpSysGroup})