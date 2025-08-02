_D='tmnxPtpLogSyncInterval'
_C='TIMETRA-SAS-PTP-MIB'
_B='current'
_A='TmnxPtpLogInterval'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowPointer','RowStatus','TextualConvention','TimeStamp','TruthValue')
tmnxChassisNotifyChassisId,tmnxChassisNotifyHwIndex,tmnxCpmCardEntry,tmnxCpmCardOscillatorType=mibBuilder.importSymbols('TIMETRA-CHASSIS-MIB','tmnxChassisNotifyChassisId','tmnxChassisNotifyHwIndex','tmnxCpmCardEntry','tmnxCpmCardOscillatorType')
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TmnxPtpLogInterval,=mibBuilder.importSymbols('TIMETRA-PTP-MIB',_A)
timetraSASConfs,timetraSASModules,timetraSASNotifyPrefix,timetraSASObjs=mibBuilder.importSymbols('TIMETRA-SAS-GLOBAL-MIB','timetraSASConfs','timetraSASModules','timetraSASNotifyPrefix','timetraSASObjs')
TItemDescription,TmnxAdminState,TmnxOperState=mibBuilder.importSymbols('TIMETRA-TC-MIB','TItemDescription','TmnxAdminState','TmnxOperState')
vRtrID,=mibBuilder.importSymbols('TIMETRA-VRTR-MIB','vRtrID')
timetraSASPtpMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,2,1,1,74))
if mibBuilder.loadTexts:timetraSASPtpMIBModule.setRevisions(('2011-02-01 00:00',))
_TmnxSASPtpGroups_ObjectIdentity=ObjectIdentity
tmnxSASPtpGroups=_TmnxSASPtpGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,74))
_TmnxSASPtp1588Objs_ObjectIdentity=ObjectIdentity
tmnxSASPtp1588Objs=_TmnxSASPtp1588Objs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,74))
_TmnxSASPtpClockConfig_ObjectIdentity=ObjectIdentity
tmnxSASPtpClockConfig=_TmnxSASPtpClockConfig_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,74,1))
class _TmnxPtpLogSyncInterval_Type(TmnxPtpLogInterval):defaultValue=-6;subtypeSpec=TmnxPtpLogInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-6,-3))
_TmnxPtpLogSyncInterval_Type.__name__=_A
_TmnxPtpLogSyncInterval_Object=MibScalar
tmnxPtpLogSyncInterval=_TmnxPtpLogSyncInterval_Object((1,3,6,1,4,1,6527,6,2,2,2,74,1,1),_TmnxPtpLogSyncInterval_Type())
tmnxPtpLogSyncInterval.setMaxAccess('read-write')
if mibBuilder.loadTexts:tmnxPtpLogSyncInterval.setStatus(_B)
tmnxSASPtpV5v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,74,1))
tmnxSASPtpV5v0Group.setObjects((_C,_D))
if mibBuilder.loadTexts:tmnxSASPtpV5v0Group.setStatus(_B)
mibBuilder.exportSymbols(_C,**{'timetraSASPtpMIBModule':timetraSASPtpMIBModule,'tmnxSASPtpGroups':tmnxSASPtpGroups,'tmnxSASPtpV5v0Group':tmnxSASPtpV5v0Group,'tmnxSASPtp1588Objs':tmnxSASPtp1588Objs,'tmnxSASPtpClockConfig':tmnxSASPtpClockConfig,_D:tmnxPtpLogSyncInterval})