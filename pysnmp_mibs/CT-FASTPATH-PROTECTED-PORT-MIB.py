_E='read-write'
_D='ctAgentSwitchProtectedPortGroupId'
_C='CT-FASTPATH-PROTECTED-PORT-MIB'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctFastPathProtectedPortMib,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctFastPathProtectedPortMib')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_B,'PhysAddress','TextualConvention')
ctFastPathProtectedPortMIB=ModuleIdentity((1,3,6,1,4,1,52,4,2,33,1))
if mibBuilder.loadTexts:ctFastPathProtectedPortMIB.setRevisions(('2006-03-06 15:01',))
_CtAgentSwitchConfigGroup_ObjectIdentity=ObjectIdentity
ctAgentSwitchConfigGroup=_CtAgentSwitchConfigGroup_ObjectIdentity((1,3,6,1,4,1,52,4,2,33,1,1))
_CtAgentSwitchProtectedPortConfigGroup_ObjectIdentity=ObjectIdentity
ctAgentSwitchProtectedPortConfigGroup=_CtAgentSwitchProtectedPortConfigGroup_ObjectIdentity((1,3,6,1,4,1,52,4,2,33,1,1,18))
_CtAgentSwitchProtectedPortTable_Object=MibTable
ctAgentSwitchProtectedPortTable=_CtAgentSwitchProtectedPortTable_Object((1,3,6,1,4,1,52,4,2,33,1,1,18,1))
if mibBuilder.loadTexts:ctAgentSwitchProtectedPortTable.setStatus(_A)
_CtAgentSwitchProtectedPortEntry_Object=MibTableRow
ctAgentSwitchProtectedPortEntry=_CtAgentSwitchProtectedPortEntry_Object((1,3,6,1,4,1,52,4,2,33,1,1,18,1,1))
ctAgentSwitchProtectedPortEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ctAgentSwitchProtectedPortEntry.setStatus(_A)
_CtAgentSwitchProtectedPortGroupId_Type=Integer32
_CtAgentSwitchProtectedPortGroupId_Object=MibTableColumn
ctAgentSwitchProtectedPortGroupId=_CtAgentSwitchProtectedPortGroupId_Object((1,3,6,1,4,1,52,4,2,33,1,1,18,1,1,1),_CtAgentSwitchProtectedPortGroupId_Type())
ctAgentSwitchProtectedPortGroupId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ctAgentSwitchProtectedPortGroupId.setStatus(_A)
class _CtAgentSwitchProtectedPortGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CtAgentSwitchProtectedPortGroupName_Type.__name__=_B
_CtAgentSwitchProtectedPortGroupName_Object=MibTableColumn
ctAgentSwitchProtectedPortGroupName=_CtAgentSwitchProtectedPortGroupName_Object((1,3,6,1,4,1,52,4,2,33,1,1,18,1,1,2),_CtAgentSwitchProtectedPortGroupName_Type())
ctAgentSwitchProtectedPortGroupName.setMaxAccess(_E)
if mibBuilder.loadTexts:ctAgentSwitchProtectedPortGroupName.setStatus(_A)
_CtAgentSwitchProtectedPortPortList_Type=PortList
_CtAgentSwitchProtectedPortPortList_Object=MibTableColumn
ctAgentSwitchProtectedPortPortList=_CtAgentSwitchProtectedPortPortList_Object((1,3,6,1,4,1,52,4,2,33,1,1,18,1,1,3),_CtAgentSwitchProtectedPortPortList_Type())
ctAgentSwitchProtectedPortPortList.setMaxAccess(_E)
if mibBuilder.loadTexts:ctAgentSwitchProtectedPortPortList.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ctFastPathProtectedPortMIB':ctFastPathProtectedPortMIB,'ctAgentSwitchConfigGroup':ctAgentSwitchConfigGroup,'ctAgentSwitchProtectedPortConfigGroup':ctAgentSwitchProtectedPortConfigGroup,'ctAgentSwitchProtectedPortTable':ctAgentSwitchProtectedPortTable,'ctAgentSwitchProtectedPortEntry':ctAgentSwitchProtectedPortEntry,_D:ctAgentSwitchProtectedPortGroupId,'ctAgentSwitchProtectedPortGroupName':ctAgentSwitchProtectedPortGroupName,'ctAgentSwitchProtectedPortPortList':ctAgentSwitchProtectedPortPortList})