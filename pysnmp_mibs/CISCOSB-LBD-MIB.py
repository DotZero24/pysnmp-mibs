_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rlLbd=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,127))
if mibBuilder.loadTexts:rlLbd.setRevisions(('2007-11-07 00:00',))
_RlLbdEnable_Type=TruthValue
_RlLbdEnable_Object=MibScalar
rlLbdEnable=_RlLbdEnable_Object((1,3,6,1,4,1,9,6,1,101,127,1),_RlLbdEnable_Type())
rlLbdEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLbdEnable.setStatus(_A)
class _RlLbdDetectionInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,60))
_RlLbdDetectionInterval_Type.__name__=_B
_RlLbdDetectionInterval_Object=MibScalar
rlLbdDetectionInterval=_RlLbdDetectionInterval_Object((1,3,6,1,4,1,9,6,1,101,127,2),_RlLbdDetectionInterval_Type())
rlLbdDetectionInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLbdDetectionInterval.setStatus(_A)
if mibBuilder.loadTexts:rlLbdDetectionInterval.setUnits('seconds')
class _RlLbdMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('source-mac-addr',1),('base-mac-addr',2),('broadcast-mac-addr',3),('predefined-multicast-mac-addr',4),('user-defined-mac-addr',5)))
_RlLbdMode_Type.__name__=_B
_RlLbdMode_Object=MibScalar
rlLbdMode=_RlLbdMode_Object((1,3,6,1,4,1,9,6,1,101,127,3),_RlLbdMode_Type())
rlLbdMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLbdMode.setStatus(_A)
_RlLbdPortTable_Object=MibTable
rlLbdPortTable=_RlLbdPortTable_Object((1,3,6,1,4,1,9,6,1,101,127,4))
if mibBuilder.loadTexts:rlLbdPortTable.setStatus(_A)
_RlLbdPortEntry_Object=MibTableRow
rlLbdPortEntry=_RlLbdPortEntry_Object((1,3,6,1,4,1,9,6,1,101,127,4,1))
rlLbdPortEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlLbdPortEntry.setStatus(_A)
class _RlLbdPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_RlLbdPortAdminStatus_Type.__name__=_B
_RlLbdPortAdminStatus_Object=MibTableColumn
rlLbdPortAdminStatus=_RlLbdPortAdminStatus_Object((1,3,6,1,4,1,9,6,1,101,127,4,1,1),_RlLbdPortAdminStatus_Type())
rlLbdPortAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlLbdPortAdminStatus.setStatus(_A)
class _RlLbdPortOperStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inactive',1),('active',2),('loopDetected',3)))
_RlLbdPortOperStatus_Type.__name__=_B
_RlLbdPortOperStatus_Object=MibTableColumn
rlLbdPortOperStatus=_RlLbdPortOperStatus_Object((1,3,6,1,4,1,9,6,1,101,127,4,1,2),_RlLbdPortOperStatus_Type())
rlLbdPortOperStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlLbdPortOperStatus.setStatus(_A)
mibBuilder.exportSymbols('CISCOSB-LBD-MIB',**{'rlLbd':rlLbd,'rlLbdEnable':rlLbdEnable,'rlLbdDetectionInterval':rlLbdDetectionInterval,'rlLbdMode':rlLbdMode,'rlLbdPortTable':rlLbdPortTable,'rlLbdPortEntry':rlLbdPortEntry,'rlLbdPortAdminStatus':rlLbdPortAdminStatus,'rlLbdPortOperStatus':rlLbdPortOperStatus})