_I='rlErrdisableRecoveryCause'
_H='CISCOSB-ERRDISABLE-RECOVERY-MIB'
_G='seconds'
_F='read-write'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
rlErrdisableRecovery=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,128))
if mibBuilder.loadTexts:rlErrdisableRecovery.setRevisions(('2007-11-07 00:00',))
class RlErrdisableRecoveryCauseType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('loopback-detection',1),('port-security',2),('dot1x-src-address',3),('acl-deny',4),('stp-bpdu-guard',5),('stp-loopback-guard',6),('pcb-overheat',7),('udld',8),('storm-control',9),('link-flapping',10)))
class _RlErrdisableRecoveryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,86400))
_RlErrdisableRecoveryInterval_Type.__name__=_E
_RlErrdisableRecoveryInterval_Object=MibScalar
rlErrdisableRecoveryInterval=_RlErrdisableRecoveryInterval_Object((1,3,6,1,4,1,9,6,1,101,128,1),_RlErrdisableRecoveryInterval_Type())
rlErrdisableRecoveryInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:rlErrdisableRecoveryInterval.setStatus(_A)
if mibBuilder.loadTexts:rlErrdisableRecoveryInterval.setUnits(_G)
_RlErrdisableRecoveryCauseTable_Object=MibTable
rlErrdisableRecoveryCauseTable=_RlErrdisableRecoveryCauseTable_Object((1,3,6,1,4,1,9,6,1,101,128,2))
if mibBuilder.loadTexts:rlErrdisableRecoveryCauseTable.setStatus(_A)
_RlErrdisableRecoveryCauseEntry_Object=MibTableRow
rlErrdisableRecoveryCauseEntry=_RlErrdisableRecoveryCauseEntry_Object((1,3,6,1,4,1,9,6,1,101,128,2,1))
rlErrdisableRecoveryCauseEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:rlErrdisableRecoveryCauseEntry.setStatus(_A)
_RlErrdisableRecoveryCause_Type=RlErrdisableRecoveryCauseType
_RlErrdisableRecoveryCause_Object=MibTableColumn
rlErrdisableRecoveryCause=_RlErrdisableRecoveryCause_Object((1,3,6,1,4,1,9,6,1,101,128,2,1,1),_RlErrdisableRecoveryCause_Type())
rlErrdisableRecoveryCause.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rlErrdisableRecoveryCause.setStatus(_A)
_RlErrdisableRecoveryEnable_Type=TruthValue
_RlErrdisableRecoveryEnable_Object=MibTableColumn
rlErrdisableRecoveryEnable=_RlErrdisableRecoveryEnable_Object((1,3,6,1,4,1,9,6,1,101,128,2,1,2),_RlErrdisableRecoveryEnable_Type())
rlErrdisableRecoveryEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:rlErrdisableRecoveryEnable.setStatus(_A)
_RlErrdisableRecoveryIfTable_Object=MibTable
rlErrdisableRecoveryIfTable=_RlErrdisableRecoveryIfTable_Object((1,3,6,1,4,1,9,6,1,101,128,3))
if mibBuilder.loadTexts:rlErrdisableRecoveryIfTable.setStatus(_A)
_RlErrdisableRecoveryIfEntry_Object=MibTableRow
rlErrdisableRecoveryIfEntry=_RlErrdisableRecoveryIfEntry_Object((1,3,6,1,4,1,9,6,1,101,128,3,1))
rlErrdisableRecoveryIfEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:rlErrdisableRecoveryIfEntry.setStatus(_A)
_RlErrdisableRecoveryIfReason_Type=RlErrdisableRecoveryCauseType
_RlErrdisableRecoveryIfReason_Object=MibTableColumn
rlErrdisableRecoveryIfReason=_RlErrdisableRecoveryIfReason_Object((1,3,6,1,4,1,9,6,1,101,128,3,1,1),_RlErrdisableRecoveryIfReason_Type())
rlErrdisableRecoveryIfReason.setMaxAccess(_B)
if mibBuilder.loadTexts:rlErrdisableRecoveryIfReason.setStatus(_A)
_RlErrdisableRecoveryIfEnable_Type=TruthValue
_RlErrdisableRecoveryIfEnable_Object=MibTableColumn
rlErrdisableRecoveryIfEnable=_RlErrdisableRecoveryIfEnable_Object((1,3,6,1,4,1,9,6,1,101,128,3,1,2),_RlErrdisableRecoveryIfEnable_Type())
rlErrdisableRecoveryIfEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlErrdisableRecoveryIfEnable.setStatus(_A)
_RlErrdisableRecoveryIfTimeToRecover_Type=Integer32
_RlErrdisableRecoveryIfTimeToRecover_Object=MibTableColumn
rlErrdisableRecoveryIfTimeToRecover=_RlErrdisableRecoveryIfTimeToRecover_Object((1,3,6,1,4,1,9,6,1,101,128,3,1,3),_RlErrdisableRecoveryIfTimeToRecover_Type())
rlErrdisableRecoveryIfTimeToRecover.setMaxAccess(_B)
if mibBuilder.loadTexts:rlErrdisableRecoveryIfTimeToRecover.setStatus(_A)
if mibBuilder.loadTexts:rlErrdisableRecoveryIfTimeToRecover.setUnits(_G)
mibBuilder.exportSymbols(_H,**{'RlErrdisableRecoveryCauseType':RlErrdisableRecoveryCauseType,'rlErrdisableRecovery':rlErrdisableRecovery,'rlErrdisableRecoveryInterval':rlErrdisableRecoveryInterval,'rlErrdisableRecoveryCauseTable':rlErrdisableRecoveryCauseTable,'rlErrdisableRecoveryCauseEntry':rlErrdisableRecoveryCauseEntry,_I:rlErrdisableRecoveryCause,'rlErrdisableRecoveryEnable':rlErrdisableRecoveryEnable,'rlErrdisableRecoveryIfTable':rlErrdisableRecoveryIfTable,'rlErrdisableRecoveryIfEntry':rlErrdisableRecoveryIfEntry,'rlErrdisableRecoveryIfReason':rlErrdisableRecoveryIfReason,'rlErrdisableRecoveryIfEnable':rlErrdisableRecoveryIfEnable,'rlErrdisableRecoveryIfTimeToRecover':rlErrdisableRecoveryIfTimeToRecover})