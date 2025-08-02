_I='oacBridgeGroupInterfaceName'
_H='TruthValue'
_G='ifIndex'
_F='IF-MIB'
_E='oacBridgeGroupValue'
_D='Unsigned32'
_C='ONEACCESS-BRIDGE-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_F,'InterfaceIndex',_G)
oacExpIMIp,oacMIBModules=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMIp','oacMIBModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_H)
oacBridgeMIB=ModuleIdentity((1,3,6,1,4,1,13191,1,100,682))
if mibBuilder.loadTexts:oacBridgeMIB.setRevisions(('2011-06-15 00:00','2010-07-08 10:00'))
_OacBridgeObjects_ObjectIdentity=ObjectIdentity
oacBridgeObjects=_OacBridgeObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,7))
_OacBridgeConfigObjects_ObjectIdentity=ObjectIdentity
oacBridgeConfigObjects=_OacBridgeConfigObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,7,1))
_OacBridgeGroupTable_Object=MibTable
oacBridgeGroupTable=_OacBridgeGroupTable_Object((1,3,6,1,4,1,13191,10,3,1,7,1,1))
if mibBuilder.loadTexts:oacBridgeGroupTable.setStatus(_A)
_OacBridgeGroupEntry_Object=MibTableRow
oacBridgeGroupEntry=_OacBridgeGroupEntry_Object((1,3,6,1,4,1,13191,10,3,1,7,1,1,1))
oacBridgeGroupEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:oacBridgeGroupEntry.setStatus(_A)
class _OacBridgeGroupValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OacBridgeGroupValue_Type.__name__=_D
_OacBridgeGroupValue_Object=MibTableColumn
oacBridgeGroupValue=_OacBridgeGroupValue_Object((1,3,6,1,4,1,13191,10,3,1,7,1,1,1,1),_OacBridgeGroupValue_Type())
oacBridgeGroupValue.setMaxAccess(_B)
if mibBuilder.loadTexts:oacBridgeGroupValue.setStatus(_A)
class _OacBridgeTransparency_Type(TruthValue):defaultValue=2
_OacBridgeTransparency_Type.__name__=_H
_OacBridgeTransparency_Object=MibTableColumn
oacBridgeTransparency=_OacBridgeTransparency_Object((1,3,6,1,4,1,13191,10,3,1,7,1,1,1,2),_OacBridgeTransparency_Type())
oacBridgeTransparency.setMaxAccess(_B)
if mibBuilder.loadTexts:oacBridgeTransparency.setStatus(_A)
_OacBridgeGroupRowStatus_Type=RowStatus
_OacBridgeGroupRowStatus_Object=MibTableColumn
oacBridgeGroupRowStatus=_OacBridgeGroupRowStatus_Object((1,3,6,1,4,1,13191,10,3,1,7,1,1,1,3),_OacBridgeGroupRowStatus_Type())
oacBridgeGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oacBridgeGroupRowStatus.setStatus(_A)
_OacBridgeGroupInterfaceTable_Object=MibTable
oacBridgeGroupInterfaceTable=_OacBridgeGroupInterfaceTable_Object((1,3,6,1,4,1,13191,10,3,1,7,1,2))
if mibBuilder.loadTexts:oacBridgeGroupInterfaceTable.setStatus(_A)
_OacBridgeGroupInterfaceEntry_Object=MibTableRow
oacBridgeGroupInterfaceEntry=_OacBridgeGroupInterfaceEntry_Object((1,3,6,1,4,1,13191,10,3,1,7,1,2,1))
oacBridgeGroupInterfaceEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:oacBridgeGroupInterfaceEntry.setStatus(_A)
class _OacInBridgeGroupValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OacInBridgeGroupValue_Type.__name__=_D
_OacInBridgeGroupValue_Object=MibTableColumn
oacInBridgeGroupValue=_OacInBridgeGroupValue_Object((1,3,6,1,4,1,13191,10,3,1,7,1,2,1,1),_OacInBridgeGroupValue_Type())
oacInBridgeGroupValue.setMaxAccess(_B)
if mibBuilder.loadTexts:oacInBridgeGroupValue.setStatus(_A)
_OacBridgeGroupInterfaceName_Type=DisplayString
_OacBridgeGroupInterfaceName_Object=MibTableColumn
oacBridgeGroupInterfaceName=_OacBridgeGroupInterfaceName_Object((1,3,6,1,4,1,13191,10,3,1,7,1,2,1,2),_OacBridgeGroupInterfaceName_Type())
oacBridgeGroupInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:oacBridgeGroupInterfaceName.setStatus(_A)
_OacBridgeGroupInterfaceRowStatus_Type=RowStatus
_OacBridgeGroupInterfaceRowStatus_Object=MibTableColumn
oacBridgeGroupInterfaceRowStatus=_OacBridgeGroupInterfaceRowStatus_Object((1,3,6,1,4,1,13191,10,3,1,7,1,2,1,3),_OacBridgeGroupInterfaceRowStatus_Type())
oacBridgeGroupInterfaceRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oacBridgeGroupInterfaceRowStatus.setStatus(_A)
_OacBridgeConformance_ObjectIdentity=ObjectIdentity
oacBridgeConformance=_OacBridgeConformance_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,7,10))
_OacBridgeGroupConfigGroups_ObjectIdentity=ObjectIdentity
oacBridgeGroupConfigGroups=_OacBridgeGroupConfigGroups_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,7,10,1))
_OacBridgeGroupCompls_ObjectIdentity=ObjectIdentity
oacBridgeGroupCompls=_OacBridgeGroupCompls_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,7,10,2))
oacBridgeGroupConfigGroup=ObjectGroup((1,3,6,1,4,1,13191,10,3,1,7,10,1,1))
oacBridgeGroupConfigGroup.setObjects(*((_C,_E),(_C,_I)))
if mibBuilder.loadTexts:oacBridgeGroupConfigGroup.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'oacBridgeMIB':oacBridgeMIB,'oacBridgeObjects':oacBridgeObjects,'oacBridgeConfigObjects':oacBridgeConfigObjects,'oacBridgeGroupTable':oacBridgeGroupTable,'oacBridgeGroupEntry':oacBridgeGroupEntry,_E:oacBridgeGroupValue,'oacBridgeTransparency':oacBridgeTransparency,'oacBridgeGroupRowStatus':oacBridgeGroupRowStatus,'oacBridgeGroupInterfaceTable':oacBridgeGroupInterfaceTable,'oacBridgeGroupInterfaceEntry':oacBridgeGroupInterfaceEntry,'oacInBridgeGroupValue':oacInBridgeGroupValue,_I:oacBridgeGroupInterfaceName,'oacBridgeGroupInterfaceRowStatus':oacBridgeGroupInterfaceRowStatus,'oacBridgeConformance':oacBridgeConformance,'oacBridgeGroupConfigGroups':oacBridgeGroupConfigGroups,'oacBridgeGroupConfigGroup':oacBridgeGroupConfigGroup,'oacBridgeGroupCompls':oacBridgeGroupCompls})