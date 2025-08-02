_F='ifIndex'
_E='NMS-POE-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nmslocal,=mibBuilder.importSymbols('NMS-SMI','nmslocal')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
_Poe_ObjectIdentity=ObjectIdentity
poe=_Poe_ObjectIdentity((1,3,6,1,4,1,3320,2,236))
_PowerEtherTable_Object=MibTable
powerEtherTable=_PowerEtherTable_Object((1,3,6,1,4,1,3320,2,236,1))
if mibBuilder.loadTexts:powerEtherTable.setStatus(_A)
_PowerEtherTableEntry_Object=MibTableRow
powerEtherTableEntry=_PowerEtherTableEntry_Object((1,3,6,1,4,1,3320,2,236,1,1))
powerEtherTableEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:powerEtherTableEntry.setStatus(_A)
_IfIndex_Type=Integer32
_IfIndex_Object=MibTableColumn
ifIndex=_IfIndex_Object((1,3,6,1,4,1,3320,2,236,1,1,1),_IfIndex_Type())
ifIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ifIndex.setStatus(_A)
class _IfDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IfDescr_Type.__name__=_D
_IfDescr_Object=MibTableColumn
ifDescr=_IfDescr_Object((1,3,6,1,4,1,3320,2,236,1,1,2),_IfDescr_Type())
ifDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:ifDescr.setStatus(_A)
_IfPethPortControlAbility_Type=TruthValue
_IfPethPortControlAbility_Object=MibTableColumn
ifPethPortControlAbility=_IfPethPortControlAbility_Object((1,3,6,1,4,1,3320,2,236,1,1,3),_IfPethPortControlAbility_Type())
ifPethPortControlAbility.setMaxAccess(_B)
if mibBuilder.loadTexts:ifPethPortControlAbility.setStatus(_A)
class _IfPethPortMaxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_IfPethPortMaxPower_Type.__name__=_C
_IfPethPortMaxPower_Object=MibTableColumn
ifPethPortMaxPower=_IfPethPortMaxPower_Object((1,3,6,1,4,1,3320,2,236,1,1,4),_IfPethPortMaxPower_Type())
ifPethPortMaxPower.setMaxAccess('read-write')
if mibBuilder.loadTexts:ifPethPortMaxPower.setStatus(_A)
_IfPethPortConsumptionPower_Type=Integer32
_IfPethPortConsumptionPower_Object=MibTableColumn
ifPethPortConsumptionPower=_IfPethPortConsumptionPower_Object((1,3,6,1,4,1,3320,2,236,1,1,5),_IfPethPortConsumptionPower_Type())
ifPethPortConsumptionPower.setMaxAccess(_B)
if mibBuilder.loadTexts:ifPethPortConsumptionPower.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'poe':poe,'powerEtherTable':powerEtherTable,'powerEtherTableEntry':powerEtherTableEntry,_F:ifIndex,'ifDescr':ifDescr,'ifPethPortControlAbility':ifPethPortControlAbility,'ifPethPortMaxPower':ifPethPortMaxPower,'ifPethPortConsumptionPower':ifPethPortConsumptionPower})