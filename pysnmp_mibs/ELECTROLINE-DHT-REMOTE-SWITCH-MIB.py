_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dhtExtensionsMibObjects,=mibBuilder.importSymbols('ELECTROLINE-DHT-EXTENSIONS-MIB','dhtExtensionsMibObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
dhtRemoteSwitchMib=ModuleIdentity((1,3,6,1,4,1,5802,1,3,1,2,5,1,11))
if mibBuilder.loadTexts:dhtRemoteSwitchMib.setRevisions(('2004-12-10 00:00',))
_DhtRemoteSwitchObjects_ObjectIdentity=ObjectIdentity
dhtRemoteSwitchObjects=_DhtRemoteSwitchObjects_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,5,1,11,1))
_DhtRemoteSwitchPresence_Type=TruthValue
_DhtRemoteSwitchPresence_Object=MibScalar
dhtRemoteSwitchPresence=_DhtRemoteSwitchPresence_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,11,1,1),_DhtRemoteSwitchPresence_Type())
dhtRemoteSwitchPresence.setMaxAccess(_D)
if mibBuilder.loadTexts:dhtRemoteSwitchPresence.setStatus(_A)
_DhtRemoteSwitchManagement_ObjectIdentity=ObjectIdentity
dhtRemoteSwitchManagement=_DhtRemoteSwitchManagement_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,5,1,11,1,11))
class _DhtRemoteSwitchControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_DhtRemoteSwitchControl_Type.__name__=_B
_DhtRemoteSwitchControl_Object=MibScalar
dhtRemoteSwitchControl=_DhtRemoteSwitchControl_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,11,1,11,1),_DhtRemoteSwitchControl_Type())
dhtRemoteSwitchControl.setMaxAccess(_C)
if mibBuilder.loadTexts:dhtRemoteSwitchControl.setStatus(_A)
class _DhtRemoteSwitchAutoStopTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,120))
_DhtRemoteSwitchAutoStopTimer_Type.__name__=_B
_DhtRemoteSwitchAutoStopTimer_Object=MibScalar
dhtRemoteSwitchAutoStopTimer=_DhtRemoteSwitchAutoStopTimer_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,11,1,11,2),_DhtRemoteSwitchAutoStopTimer_Type())
dhtRemoteSwitchAutoStopTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:dhtRemoteSwitchAutoStopTimer.setStatus(_A)
class _DhtRemoteSwitchStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('on',1),('off',2),('mismatch',3),('timeout',4)))
_DhtRemoteSwitchStatus_Type.__name__=_B
_DhtRemoteSwitchStatus_Object=MibScalar
dhtRemoteSwitchStatus=_DhtRemoteSwitchStatus_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,11,1,11,3),_DhtRemoteSwitchStatus_Type())
dhtRemoteSwitchStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dhtRemoteSwitchStatus.setStatus(_A)
_DhtRemoteSwitchOnTime_Type=Counter32
_DhtRemoteSwitchOnTime_Object=MibScalar
dhtRemoteSwitchOnTime=_DhtRemoteSwitchOnTime_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,11,1,11,4),_DhtRemoteSwitchOnTime_Type())
dhtRemoteSwitchOnTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dhtRemoteSwitchOnTime.setStatus(_A)
mibBuilder.exportSymbols('ELECTROLINE-DHT-REMOTE-SWITCH-MIB',**{'dhtRemoteSwitchMib':dhtRemoteSwitchMib,'dhtRemoteSwitchObjects':dhtRemoteSwitchObjects,'dhtRemoteSwitchPresence':dhtRemoteSwitchPresence,'dhtRemoteSwitchManagement':dhtRemoteSwitchManagement,'dhtRemoteSwitchControl':dhtRemoteSwitchControl,'dhtRemoteSwitchAutoStopTimer':dhtRemoteSwitchAutoStopTimer,'dhtRemoteSwitchStatus':dhtRemoteSwitchStatus,'dhtRemoteSwitchOnTime':dhtRemoteSwitchOnTime})