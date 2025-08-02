_E='current'
_D='read-write'
_C='disabled'
_B='enabled'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cmtsC3,=mibBuilder.importSymbols('ARRIS-MIB','cmtsC3')
TenthdBmV,docsIfCmtsCmStatusEntry=mibBuilder.importSymbols('DOCS-IF-MIB','TenthdBmV','docsIfCmtsCmStatusEntry')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
cmtsC3RngMIB=ModuleIdentity((1,3,6,1,4,1,4115,1,4,3,10))
_PhoenixRangingGroup_ObjectIdentity=ObjectIdentity
phoenixRangingGroup=_PhoenixRangingGroup_ObjectIdentity((1,3,6,1,4,1,4115,1,4,3,10,1))
class _PhxRangingPowerOverride_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_B,1),(_C,2)))
_PhxRangingPowerOverride_Type.__name__=_A
_PhxRangingPowerOverride_Object=MibScalar
phxRangingPowerOverride=_PhxRangingPowerOverride_Object((1,3,6,1,4,1,4115,1,4,3,10,1,1),_PhxRangingPowerOverride_Type())
phxRangingPowerOverride.setMaxAccess(_D)
if mibBuilder.loadTexts:phxRangingPowerOverride.setStatus(_E)
class _PhxRangingForceContinue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_C,0),(_B,1)))
_PhxRangingForceContinue_Type.__name__=_A
_PhxRangingForceContinue_Object=MibScalar
phxRangingForceContinue=_PhxRangingForceContinue_Object((1,3,6,1,4,1,4115,1,4,3,10,1,2),_PhxRangingForceContinue_Type())
phxRangingForceContinue.setMaxAccess(_D)
if mibBuilder.loadTexts:phxRangingForceContinue.setStatus(_E)
mibBuilder.exportSymbols('ARRIS-C3-RANGING-MIB',**{'cmtsC3RngMIB':cmtsC3RngMIB,'phoenixRangingGroup':phoenixRangingGroup,'phxRangingPowerOverride':phxRangingPowerOverride,'phxRangingForceContinue':phxRangingForceContinue})