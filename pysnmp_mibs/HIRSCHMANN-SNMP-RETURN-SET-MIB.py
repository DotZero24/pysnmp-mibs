_H='hmMgmtSEParameterID'
_G='read-only'
_F='not-accessible'
_E='read-write'
_D='Integer32'
_C='hmMgmtSeReturnKey'
_B='HIRSCHMANN-SNMP-RETURN-SET-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention,TestAndIncr=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','TextualConvention','TestAndIncr')
hmMgmtSEReturnSetGroup=ModuleIdentity((1,3,6,1,4,1,248,16,1,1))
if mibBuilder.loadTexts:hmMgmtSEReturnSetGroup.setRevisions(('2010-09-14 12:00',))
_Hirschmann_ObjectIdentity=ObjectIdentity
hirschmann=_Hirschmann_ObjectIdentity((1,3,6,1,4,1,248))
_HmMgmtSNMPExtensionGroup_ObjectIdentity=ObjectIdentity
hmMgmtSNMPExtensionGroup=_HmMgmtSNMPExtensionGroup_ObjectIdentity((1,3,6,1,4,1,248,16,1))
_HmMgmtSESReturns_ObjectIdentity=ObjectIdentity
hmMgmtSESReturns=_HmMgmtSESReturns_ObjectIdentity((1,3,6,1,4,1,248,16,1,1,1))
if mibBuilder.loadTexts:hmMgmtSESReturns.setStatus(_A)
_HmMgmtSESOkReturn_ObjectIdentity=ObjectIdentity
hmMgmtSESOkReturn=_HmMgmtSESOkReturn_ObjectIdentity((1,3,6,1,4,1,248,16,1,1,1,1))
if mibBuilder.loadTexts:hmMgmtSESOkReturn.setStatus(_A)
_HmMgmtSESPendingReturn_ObjectIdentity=ObjectIdentity
hmMgmtSESPendingReturn=_HmMgmtSESPendingReturn_ObjectIdentity((1,3,6,1,4,1,248,16,1,1,1,2))
if mibBuilder.loadTexts:hmMgmtSESPendingReturn.setStatus(_A)
_HmMgmtSESFailureReturn_ObjectIdentity=ObjectIdentity
hmMgmtSESFailureReturn=_HmMgmtSESFailureReturn_ObjectIdentity((1,3,6,1,4,1,248,16,1,1,1,3))
if mibBuilder.loadTexts:hmMgmtSESFailureReturn.setStatus(_A)
_HmMgmtSESTestReturn_ObjectIdentity=ObjectIdentity
hmMgmtSESTestReturn=_HmMgmtSESTestReturn_ObjectIdentity((1,3,6,1,4,1,248,16,1,1,1,100))
if mibBuilder.loadTexts:hmMgmtSESTestReturn.setStatus(_A)
_HmMgmtSESpinLock_Type=TestAndIncr
_HmMgmtSESpinLock_Object=MibScalar
hmMgmtSESpinLock=_HmMgmtSESpinLock_Object((1,3,6,1,4,1,248,16,1,1,2),_HmMgmtSESpinLock_Type())
hmMgmtSESpinLock.setMaxAccess(_E)
if mibBuilder.loadTexts:hmMgmtSESpinLock.setStatus(_A)
_HmMgmtSEReturnTable_Object=MibTable
hmMgmtSEReturnTable=_HmMgmtSEReturnTable_Object((1,3,6,1,4,1,248,16,1,1,3))
if mibBuilder.loadTexts:hmMgmtSEReturnTable.setStatus(_A)
_HmMgmtSEReturnEntry_Object=MibTableRow
hmMgmtSEReturnEntry=_HmMgmtSEReturnEntry_Object((1,3,6,1,4,1,248,16,1,1,3,1))
hmMgmtSEReturnEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:hmMgmtSEReturnEntry.setStatus(_A)
class _HmMgmtSeReturnKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HmMgmtSeReturnKey_Type.__name__=_D
_HmMgmtSeReturnKey_Object=MibTableColumn
hmMgmtSeReturnKey=_HmMgmtSeReturnKey_Object((1,3,6,1,4,1,248,16,1,1,3,1,1),_HmMgmtSeReturnKey_Type())
hmMgmtSeReturnKey.setMaxAccess(_F)
if mibBuilder.loadTexts:hmMgmtSeReturnKey.setStatus(_A)
_HmMgmtSeReturnCode_Type=AutonomousType
_HmMgmtSeReturnCode_Object=MibTableColumn
hmMgmtSeReturnCode=_HmMgmtSeReturnCode_Object((1,3,6,1,4,1,248,16,1,1,3,1,2),_HmMgmtSeReturnCode_Type())
hmMgmtSeReturnCode.setMaxAccess(_G)
if mibBuilder.loadTexts:hmMgmtSeReturnCode.setStatus(_A)
_HmMgmtSEParameterTable_Object=MibTable
hmMgmtSEParameterTable=_HmMgmtSEParameterTable_Object((1,3,6,1,4,1,248,16,1,1,4))
if mibBuilder.loadTexts:hmMgmtSEParameterTable.setStatus(_A)
_HmMgmtSEParameterEntry_Object=MibTableRow
hmMgmtSEParameterEntry=_HmMgmtSEParameterEntry_Object((1,3,6,1,4,1,248,16,1,1,4,1))
hmMgmtSEParameterEntry.setIndexNames((0,_B,_C),(0,_B,_H))
if mibBuilder.loadTexts:hmMgmtSEParameterEntry.setStatus(_A)
_HmMgmtSEParameterID_Type=Integer32
_HmMgmtSEParameterID_Object=MibTableColumn
hmMgmtSEParameterID=_HmMgmtSEParameterID_Object((1,3,6,1,4,1,248,16,1,1,4,1,1),_HmMgmtSEParameterID_Type())
hmMgmtSEParameterID.setMaxAccess(_F)
if mibBuilder.loadTexts:hmMgmtSEParameterID.setStatus(_A)
_HmMgmtSEParameterValue_Type=DisplayString
_HmMgmtSEParameterValue_Object=MibTableColumn
hmMgmtSEParameterValue=_HmMgmtSEParameterValue_Object((1,3,6,1,4,1,248,16,1,1,4,1,2),_HmMgmtSEParameterValue_Type())
hmMgmtSEParameterValue.setMaxAccess(_G)
if mibBuilder.loadTexts:hmMgmtSEParameterValue.setStatus(_A)
_HmMgmtSETestGroup_ObjectIdentity=ObjectIdentity
hmMgmtSETestGroup=_HmMgmtSETestGroup_ObjectIdentity((1,3,6,1,4,1,248,16,1,1,100))
_HmMgmtSETestVar_Type=OctetString
_HmMgmtSETestVar_Object=MibScalar
hmMgmtSETestVar=_HmMgmtSETestVar_Object((1,3,6,1,4,1,248,16,1,1,100,1),_HmMgmtSETestVar_Type())
hmMgmtSETestVar.setMaxAccess(_E)
if mibBuilder.loadTexts:hmMgmtSETestVar.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hirschmann':hirschmann,'hmMgmtSNMPExtensionGroup':hmMgmtSNMPExtensionGroup,'hmMgmtSEReturnSetGroup':hmMgmtSEReturnSetGroup,'hmMgmtSESReturns':hmMgmtSESReturns,'hmMgmtSESOkReturn':hmMgmtSESOkReturn,'hmMgmtSESPendingReturn':hmMgmtSESPendingReturn,'hmMgmtSESFailureReturn':hmMgmtSESFailureReturn,'hmMgmtSESTestReturn':hmMgmtSESTestReturn,'hmMgmtSESpinLock':hmMgmtSESpinLock,'hmMgmtSEReturnTable':hmMgmtSEReturnTable,'hmMgmtSEReturnEntry':hmMgmtSEReturnEntry,_C:hmMgmtSeReturnKey,'hmMgmtSeReturnCode':hmMgmtSeReturnCode,'hmMgmtSEParameterTable':hmMgmtSEParameterTable,'hmMgmtSEParameterEntry':hmMgmtSEParameterEntry,_H:hmMgmtSEParameterID,'hmMgmtSEParameterValue':hmMgmtSEParameterValue,'hmMgmtSETestGroup':hmMgmtSETestGroup,'hmMgmtSETestVar':hmMgmtSETestVar})