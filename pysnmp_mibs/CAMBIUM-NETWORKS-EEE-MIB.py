_E='read-only'
_D='cnEeePortIndex'
_C='CAMBIUM-NETWORKS-EEE-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
cnEeeMib=ModuleIdentity((1,3,6,1,4,1,17713,24,8))
if mibBuilder.loadTexts:cnEeeMib.setRevisions(('2021-04-19 00:00',))
_CnEeeObjects_ObjectIdentity=ObjectIdentity
cnEeeObjects=_CnEeeObjects_ObjectIdentity((1,3,6,1,4,1,17713,24,8,0))
_CnEeePortTable_Object=MibTable
cnEeePortTable=_CnEeePortTable_Object((1,3,6,1,4,1,17713,24,8,0,1))
if mibBuilder.loadTexts:cnEeePortTable.setStatus(_A)
_CnEeePortEntry_Object=MibTableRow
cnEeePortEntry=_CnEeePortEntry_Object((1,3,6,1,4,1,17713,24,8,0,1,1))
cnEeePortEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cnEeePortEntry.setStatus(_A)
class _CnEeePortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CnEeePortIndex_Type.__name__=_B
_CnEeePortIndex_Object=MibTableColumn
cnEeePortIndex=_CnEeePortIndex_Object((1,3,6,1,4,1,17713,24,8,0,1,1,1),_CnEeePortIndex_Type())
cnEeePortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cnEeePortIndex.setStatus(_A)
class _CnEeeEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_CnEeeEnabled_Type.__name__=_B
_CnEeeEnabled_Object=MibTableColumn
cnEeeEnabled=_CnEeeEnabled_Object((1,3,6,1,4,1,17713,24,8,0,1,1,2),_CnEeeEnabled_Type())
cnEeeEnabled.setMaxAccess('read-write')
if mibBuilder.loadTexts:cnEeeEnabled.setStatus(_A)
class _CnEeeCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CnEeeCapabilities_Type.__name__=_B
_CnEeeCapabilities_Object=MibTableColumn
cnEeeCapabilities=_CnEeeCapabilities_Object((1,3,6,1,4,1,17713,24,8,0,1,1,3),_CnEeeCapabilities_Type())
cnEeeCapabilities.setMaxAccess(_E)
if mibBuilder.loadTexts:cnEeeCapabilities.setStatus(_A)
class _CnEeeLpAbilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CnEeeLpAbilities_Type.__name__=_B
_CnEeeLpAbilities_Object=MibTableColumn
cnEeeLpAbilities=_CnEeeLpAbilities_Object((1,3,6,1,4,1,17713,24,8,0,1,1,4),_CnEeeLpAbilities_Type())
cnEeeLpAbilities.setMaxAccess(_E)
if mibBuilder.loadTexts:cnEeeLpAbilities.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cnEeeMib':cnEeeMib,'cnEeeObjects':cnEeeObjects,'cnEeePortTable':cnEeePortTable,'cnEeePortEntry':cnEeePortEntry,_D:cnEeePortIndex,'cnEeeEnabled':cnEeeEnabled,'cnEeeCapabilities':cnEeeCapabilities,'cnEeeLpAbilities':cnEeeLpAbilities})