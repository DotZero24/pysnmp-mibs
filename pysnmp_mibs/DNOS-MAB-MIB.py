_G='disable'
_F='enable'
_E='agentMabIfIndex'
_D='DNOS-MAB-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dnOS,=mibBuilder.importSymbols('DELL-REF-MIB','dnOS')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fastPathMab=ModuleIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,75))
if mibBuilder.loadTexts:fastPathMab.setRevisions(('2017-12-15 00:00',))
_AgentMabGlobalConfigGroup_ObjectIdentity=ObjectIdentity
agentMabGlobalConfigGroup=_AgentMabGlobalConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,75,1))
class _AgentMABRequestAttr1GroupSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,12)));namedValues=NamedValues(*(('one',1),('two',2),('four',4),('twelve',12)))
_AgentMABRequestAttr1GroupSize_Type.__name__=_B
_AgentMABRequestAttr1GroupSize_Object=MibScalar
agentMABRequestAttr1GroupSize=_AgentMABRequestAttr1GroupSize_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,75,1,1),_AgentMABRequestAttr1GroupSize_Type())
agentMABRequestAttr1GroupSize.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMABRequestAttr1GroupSize.setStatus(_A)
class _AgentMABRequestAttr1Separator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ieft',1),('legacy',2),('dot',3)))
_AgentMABRequestAttr1Separator_Type.__name__=_B
_AgentMABRequestAttr1Separator_Object=MibScalar
agentMABRequestAttr1Separator=_AgentMABRequestAttr1Separator_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,75,1,2),_AgentMABRequestAttr1Separator_Type())
agentMABRequestAttr1Separator.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMABRequestAttr1Separator.setStatus(_A)
class _AgentMABRequestAttr1Case_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upper',1),('lower',2)))
_AgentMABRequestAttr1Case_Type.__name__=_B
_AgentMABRequestAttr1Case_Object=MibScalar
agentMABRequestAttr1Case=_AgentMABRequestAttr1Case_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,75,1,3),_AgentMABRequestAttr1Case_Type())
agentMABRequestAttr1Case.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMABRequestAttr1Case.setStatus(_A)
_AgentMabPortConfigGroup_ObjectIdentity=ObjectIdentity
agentMabPortConfigGroup=_AgentMabPortConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,75,2))
_AgentMabPortConfigTable_Object=MibTable
agentMabPortConfigTable=_AgentMabPortConfigTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,75,2,1))
if mibBuilder.loadTexts:agentMabPortConfigTable.setStatus(_A)
_AgentMabPortConfigEntry_Object=MibTableRow
agentMabPortConfigEntry=_AgentMabPortConfigEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,75,2,1,1))
agentMabPortConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:agentMabPortConfigEntry.setStatus(_A)
_AgentMabIfIndex_Type=InterfaceIndex
_AgentMabIfIndex_Object=MibTableColumn
agentMabIfIndex=_AgentMabIfIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,75,2,1,1,1),_AgentMabIfIndex_Type())
agentMabIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:agentMabIfIndex.setStatus(_A)
class _AgentMABPortEnabled_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentMABPortEnabled_Type.__name__=_B
_AgentMABPortEnabled_Object=MibTableColumn
agentMABPortEnabled=_AgentMABPortEnabled_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,75,2,1,1,2),_AgentMABPortEnabled_Type())
agentMABPortEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMABPortEnabled.setStatus(_A)
class _AgentMabPortOperational_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentMabPortOperational_Type.__name__=_B
_AgentMabPortOperational_Object=MibTableColumn
agentMabPortOperational=_AgentMabPortOperational_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,75,2,1,1,3),_AgentMabPortOperational_Type())
agentMabPortOperational.setMaxAccess('read-only')
if mibBuilder.loadTexts:agentMabPortOperational.setStatus(_A)
class _AgentMabPortAuthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('eapMd5',1),('pap',2),('chap',3)))
_AgentMabPortAuthType_Type.__name__=_B
_AgentMabPortAuthType_Object=MibTableColumn
agentMabPortAuthType=_AgentMabPortAuthType_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,75,2,1,1,4),_AgentMabPortAuthType_Type())
agentMabPortAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMabPortAuthType.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fastPathMab':fastPathMab,'agentMabGlobalConfigGroup':agentMabGlobalConfigGroup,'agentMABRequestAttr1GroupSize':agentMABRequestAttr1GroupSize,'agentMABRequestAttr1Separator':agentMABRequestAttr1Separator,'agentMABRequestAttr1Case':agentMABRequestAttr1Case,'agentMabPortConfigGroup':agentMabPortConfigGroup,'agentMabPortConfigTable':agentMabPortConfigTable,'agentMabPortConfigEntry':agentMabPortConfigEntry,_E:agentMabIfIndex,'agentMABPortEnabled':agentMABPortEnabled,'agentMabPortOperational':agentMabPortOperational,'agentMabPortAuthType':agentMabPortAuthType})