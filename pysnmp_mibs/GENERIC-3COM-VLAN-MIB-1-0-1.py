_I='a3ComVlanEncapsIfIndex'
_H='a3ComVlanGlobalMappingIdentifier'
_G='DisplayString'
_F='a3ComVlanIfIndex'
_E='Integer32'
_D='read-only'
_C='GENERIC-3COM-VLAN-MIB-1-0-1'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention','TruthValue')
class RowStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
class A3ComVlanType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('vlanLayer2',1),('vlanDefaultProtocols',2),('vlanIPProtocol',3),('vlanIPXProtocol',4),('vlanAppleTalkProtocol',5),('vlanXNSProtocol',6),('vlanISOProtocol',7),('vlanDECNetProtocol',8),('vlanNetBIOSProtocol',9),('vlanSNAProtocol',10),('vlanVINESProtocol',11),('vlanX25Protocol',12),('vlanIGMPProtocol',13),('vlanSessionLayer',14),('vlanNetBeui',15)))
class A3ComVlanEncapsType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('vlanEncaps3ComProprietaryPDD',1),('vlanEncaps8021q',2),('vlanEncapsPre8021qONcore',3)))
_A3Com_ObjectIdentity=ObjectIdentity
a3Com=_A3Com_ObjectIdentity((1,3,6,1,4,1,43))
_Generic_ObjectIdentity=ObjectIdentity
generic=_Generic_ObjectIdentity((1,3,6,1,4,1,43,10))
_GenExperimental_ObjectIdentity=ObjectIdentity
genExperimental=_GenExperimental_ObjectIdentity((1,3,6,1,4,1,43,10,1))
_GenVirtual_ObjectIdentity=ObjectIdentity
genVirtual=_GenVirtual_ObjectIdentity((1,3,6,1,4,1,43,10,1,14))
_A3ComVlanGroup_ObjectIdentity=ObjectIdentity
a3ComVlanGroup=_A3ComVlanGroup_ObjectIdentity((1,3,6,1,4,1,43,10,1,14,1))
_A3ComVlanGlobalMappingTable_Object=MibTable
a3ComVlanGlobalMappingTable=_A3ComVlanGlobalMappingTable_Object((1,3,6,1,4,1,43,10,1,14,1,1))
if mibBuilder.loadTexts:a3ComVlanGlobalMappingTable.setStatus(_A)
_A3ComVlanGlobalMappingEntry_Object=MibTableRow
a3ComVlanGlobalMappingEntry=_A3ComVlanGlobalMappingEntry_Object((1,3,6,1,4,1,43,10,1,14,1,1,1))
a3ComVlanGlobalMappingEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:a3ComVlanGlobalMappingEntry.setStatus(_A)
class _A3ComVlanGlobalMappingIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_A3ComVlanGlobalMappingIdentifier_Type.__name__=_E
_A3ComVlanGlobalMappingIdentifier_Object=MibTableColumn
a3ComVlanGlobalMappingIdentifier=_A3ComVlanGlobalMappingIdentifier_Object((1,3,6,1,4,1,43,10,1,14,1,1,1,1),_A3ComVlanGlobalMappingIdentifier_Type())
a3ComVlanGlobalMappingIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComVlanGlobalMappingIdentifier.setStatus(_A)
_A3ComVlanGlobalMappingIfIndex_Type=Integer32
_A3ComVlanGlobalMappingIfIndex_Object=MibTableColumn
a3ComVlanGlobalMappingIfIndex=_A3ComVlanGlobalMappingIfIndex_Object((1,3,6,1,4,1,43,10,1,14,1,1,1,2),_A3ComVlanGlobalMappingIfIndex_Type())
a3ComVlanGlobalMappingIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComVlanGlobalMappingIfIndex.setStatus(_A)
_A3ComVlanIfTable_Object=MibTable
a3ComVlanIfTable=_A3ComVlanIfTable_Object((1,3,6,1,4,1,43,10,1,14,1,2))
if mibBuilder.loadTexts:a3ComVlanIfTable.setStatus(_A)
_A3ComVlanIfEntry_Object=MibTableRow
a3ComVlanIfEntry=_A3ComVlanIfEntry_Object((1,3,6,1,4,1,43,10,1,14,1,2,1))
a3ComVlanIfEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:a3ComVlanIfEntry.setStatus(_A)
_A3ComVlanIfIndex_Type=Integer32
_A3ComVlanIfIndex_Object=MibTableColumn
a3ComVlanIfIndex=_A3ComVlanIfIndex_Object((1,3,6,1,4,1,43,10,1,14,1,2,1,1),_A3ComVlanIfIndex_Type())
a3ComVlanIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComVlanIfIndex.setStatus(_A)
class _A3ComVlanIfDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_A3ComVlanIfDescr_Type.__name__=_G
_A3ComVlanIfDescr_Object=MibTableColumn
a3ComVlanIfDescr=_A3ComVlanIfDescr_Object((1,3,6,1,4,1,43,10,1,14,1,2,1,2),_A3ComVlanIfDescr_Type())
a3ComVlanIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComVlanIfDescr.setStatus(_A)
_A3ComVlanIfType_Type=A3ComVlanType
_A3ComVlanIfType_Object=MibTableColumn
a3ComVlanIfType=_A3ComVlanIfType_Object((1,3,6,1,4,1,43,10,1,14,1,2,1,3),_A3ComVlanIfType_Type())
a3ComVlanIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComVlanIfType.setStatus(_A)
class _A3ComVlanIfGlobalIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_A3ComVlanIfGlobalIdentifier_Type.__name__=_E
_A3ComVlanIfGlobalIdentifier_Object=MibTableColumn
a3ComVlanIfGlobalIdentifier=_A3ComVlanIfGlobalIdentifier_Object((1,3,6,1,4,1,43,10,1,14,1,2,1,4),_A3ComVlanIfGlobalIdentifier_Type())
a3ComVlanIfGlobalIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComVlanIfGlobalIdentifier.setStatus(_A)
_A3ComVlanIfInfo_Type=OctetString
_A3ComVlanIfInfo_Object=MibTableColumn
a3ComVlanIfInfo=_A3ComVlanIfInfo_Object((1,3,6,1,4,1,43,10,1,14,1,2,1,5),_A3ComVlanIfInfo_Type())
a3ComVlanIfInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComVlanIfInfo.setStatus(_A)
_A3ComVlanIfStatus_Type=RowStatus
_A3ComVlanIfStatus_Object=MibTableColumn
a3ComVlanIfStatus=_A3ComVlanIfStatus_Object((1,3,6,1,4,1,43,10,1,14,1,2,1,6),_A3ComVlanIfStatus_Type())
a3ComVlanIfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComVlanIfStatus.setStatus(_A)
_A3ComVlanIfIgnoreStpFlag_Type=TruthValue
_A3ComVlanIfIgnoreStpFlag_Object=MibTableColumn
a3ComVlanIfIgnoreStpFlag=_A3ComVlanIfIgnoreStpFlag_Object((1,3,6,1,4,1,43,10,1,14,1,2,1,7),_A3ComVlanIfIgnoreStpFlag_Type())
a3ComVlanIfIgnoreStpFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComVlanIfIgnoreStpFlag.setStatus(_A)
_A3ComVlanProtocolsGroup_ObjectIdentity=ObjectIdentity
a3ComVlanProtocolsGroup=_A3ComVlanProtocolsGroup_ObjectIdentity((1,3,6,1,4,1,43,10,1,14,2))
_A3ComIpVlanTable_Object=MibTable
a3ComIpVlanTable=_A3ComIpVlanTable_Object((1,3,6,1,4,1,43,10,1,14,2,1))
if mibBuilder.loadTexts:a3ComIpVlanTable.setStatus(_A)
_A3ComIpVlanEntry_Object=MibTableRow
a3ComIpVlanEntry=_A3ComIpVlanEntry_Object((1,3,6,1,4,1,43,10,1,14,2,1,1))
a3ComIpVlanEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:a3ComIpVlanEntry.setStatus(_A)
_A3ComIpVlanIpNetAddress_Type=IpAddress
_A3ComIpVlanIpNetAddress_Object=MibTableColumn
a3ComIpVlanIpNetAddress=_A3ComIpVlanIpNetAddress_Object((1,3,6,1,4,1,43,10,1,14,2,1,1,1),_A3ComIpVlanIpNetAddress_Type())
a3ComIpVlanIpNetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComIpVlanIpNetAddress.setStatus(_A)
_A3ComIpVlanIpNetMask_Type=IpAddress
_A3ComIpVlanIpNetMask_Object=MibTableColumn
a3ComIpVlanIpNetMask=_A3ComIpVlanIpNetMask_Object((1,3,6,1,4,1,43,10,1,14,2,1,1,2),_A3ComIpVlanIpNetMask_Type())
a3ComIpVlanIpNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComIpVlanIpNetMask.setStatus(_A)
_A3ComIpVlanStatus_Type=RowStatus
_A3ComIpVlanStatus_Object=MibTableColumn
a3ComIpVlanStatus=_A3ComIpVlanStatus_Object((1,3,6,1,4,1,43,10,1,14,2,1,1,3),_A3ComIpVlanStatus_Type())
a3ComIpVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComIpVlanStatus.setStatus(_A)
_A3ComVirtualGroup_ObjectIdentity=ObjectIdentity
a3ComVirtualGroup=_A3ComVirtualGroup_ObjectIdentity((1,3,6,1,4,1,43,10,1,14,3))
_A3ComNextAvailableVirtIfIndex_Type=Integer32
_A3ComNextAvailableVirtIfIndex_Object=MibScalar
a3ComNextAvailableVirtIfIndex=_A3ComNextAvailableVirtIfIndex_Object((1,3,6,1,4,1,43,10,1,14,3,1),_A3ComNextAvailableVirtIfIndex_Type())
a3ComNextAvailableVirtIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComNextAvailableVirtIfIndex.setStatus(_A)
_A3ComEncapsulationGroup_ObjectIdentity=ObjectIdentity
a3ComEncapsulationGroup=_A3ComEncapsulationGroup_ObjectIdentity((1,3,6,1,4,1,43,10,1,14,4))
_A3ComVlanEncapsIfTable_Object=MibTable
a3ComVlanEncapsIfTable=_A3ComVlanEncapsIfTable_Object((1,3,6,1,4,1,43,10,1,14,4,1))
if mibBuilder.loadTexts:a3ComVlanEncapsIfTable.setStatus(_A)
_A3ComVlanEncapsIfEntry_Object=MibTableRow
a3ComVlanEncapsIfEntry=_A3ComVlanEncapsIfEntry_Object((1,3,6,1,4,1,43,10,1,14,4,1,1))
a3ComVlanEncapsIfEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:a3ComVlanEncapsIfEntry.setStatus(_A)
_A3ComVlanEncapsIfIndex_Type=Integer32
_A3ComVlanEncapsIfIndex_Object=MibTableColumn
a3ComVlanEncapsIfIndex=_A3ComVlanEncapsIfIndex_Object((1,3,6,1,4,1,43,10,1,14,4,1,1,1),_A3ComVlanEncapsIfIndex_Type())
a3ComVlanEncapsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComVlanEncapsIfIndex.setStatus(_A)
_A3ComVlanEncapsIfType_Type=A3ComVlanEncapsType
_A3ComVlanEncapsIfType_Object=MibTableColumn
a3ComVlanEncapsIfType=_A3ComVlanEncapsIfType_Object((1,3,6,1,4,1,43,10,1,14,4,1,1,2),_A3ComVlanEncapsIfType_Type())
a3ComVlanEncapsIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComVlanEncapsIfType.setStatus(_A)
_A3ComVlanEncapsIfTag_Type=Integer32
_A3ComVlanEncapsIfTag_Object=MibTableColumn
a3ComVlanEncapsIfTag=_A3ComVlanEncapsIfTag_Object((1,3,6,1,4,1,43,10,1,14,4,1,1,3),_A3ComVlanEncapsIfTag_Type())
a3ComVlanEncapsIfTag.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComVlanEncapsIfTag.setStatus(_A)
_A3ComVlanEncapsIfStatus_Type=RowStatus
_A3ComVlanEncapsIfStatus_Object=MibTableColumn
a3ComVlanEncapsIfStatus=_A3ComVlanEncapsIfStatus_Object((1,3,6,1,4,1,43,10,1,14,4,1,1,4),_A3ComVlanEncapsIfStatus_Type())
a3ComVlanEncapsIfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComVlanEncapsIfStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'RowStatus':RowStatus,'A3ComVlanType':A3ComVlanType,'A3ComVlanEncapsType':A3ComVlanEncapsType,'a3Com':a3Com,'generic':generic,'genExperimental':genExperimental,'genVirtual':genVirtual,'a3ComVlanGroup':a3ComVlanGroup,'a3ComVlanGlobalMappingTable':a3ComVlanGlobalMappingTable,'a3ComVlanGlobalMappingEntry':a3ComVlanGlobalMappingEntry,_H:a3ComVlanGlobalMappingIdentifier,'a3ComVlanGlobalMappingIfIndex':a3ComVlanGlobalMappingIfIndex,'a3ComVlanIfTable':a3ComVlanIfTable,'a3ComVlanIfEntry':a3ComVlanIfEntry,_F:a3ComVlanIfIndex,'a3ComVlanIfDescr':a3ComVlanIfDescr,'a3ComVlanIfType':a3ComVlanIfType,'a3ComVlanIfGlobalIdentifier':a3ComVlanIfGlobalIdentifier,'a3ComVlanIfInfo':a3ComVlanIfInfo,'a3ComVlanIfStatus':a3ComVlanIfStatus,'a3ComVlanIfIgnoreStpFlag':a3ComVlanIfIgnoreStpFlag,'a3ComVlanProtocolsGroup':a3ComVlanProtocolsGroup,'a3ComIpVlanTable':a3ComIpVlanTable,'a3ComIpVlanEntry':a3ComIpVlanEntry,'a3ComIpVlanIpNetAddress':a3ComIpVlanIpNetAddress,'a3ComIpVlanIpNetMask':a3ComIpVlanIpNetMask,'a3ComIpVlanStatus':a3ComIpVlanStatus,'a3ComVirtualGroup':a3ComVirtualGroup,'a3ComNextAvailableVirtIfIndex':a3ComNextAvailableVirtIfIndex,'a3ComEncapsulationGroup':a3ComEncapsulationGroup,'a3ComVlanEncapsIfTable':a3ComVlanEncapsIfTable,'a3ComVlanEncapsIfEntry':a3ComVlanEncapsIfEntry,_I:a3ComVlanEncapsIfIndex,'a3ComVlanEncapsIfType':a3ComVlanEncapsIfType,'a3ComVlanEncapsIfTag':a3ComVlanEncapsIfTag,'a3ComVlanEncapsIfStatus':a3ComVlanEncapsIfStatus})