_g='alaipmReceiverVlanPortGroup'
_f='alaipmvlanCtagGroup'
_e='alaipmvlanIPAddrMaskGroup'
_d='alaipmvlanIPAddressGroup'
_c='alaipmvlanPortGroup'
_b='alaipmvReceiverVlanPortRowStatus'
_a='alaipmvVlanIpAddrMaskRowStatus'
_Z='alaipmvVlanCtagRowStatus'
_Y='alaipmvVlanIpAddrRowStatus'
_X='alaipmvVlanPortRowStatus'
_W='alaipmvReceiverVlanPortRcvrVlanNumber'
_V='alaipmvReceiverVlanPortIPMVlanNumber'
_U='alaipmvReceiverVlanPortNumber'
_T='alaipmvVlanIpAddrMaskPrefixLen'
_S='alaipmvVlanIpAddrMaskAddress'
_R='alaipmvVlanIpAddrMaskType'
_Q='alaipmvVlanIpAddrMaskVlanNumber'
_P='alaipmvVlanCtag'
_O='alaipmvVlanNumber'
_N='alaipmvVlanIpAddress'
_M='alaipmvVlanIpAddrType'
_L='alaipmvVlanIpAddrVlanNumber'
_K='alaipmvVlanPortType'
_J='alaipmvVlanPortNumber'
_I='alaipmvVlanPortIPMVlanNumber'
_H='InetAddressType'
_G='InetAddress'
_F='not-accessible'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='ALCATEL-IND1-IPM-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1IPMVlanMgt,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1IPMVlanMgt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G,'InetAddressPrefixLength',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1IPMVlanMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,41,1))
_AlcatelIND1IPMVlanMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1IPMVlanMIBObjects=_AlcatelIND1IPMVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,41,1,1))
if mibBuilder.loadTexts:alcatelIND1IPMVlanMIBObjects.setStatus(_A)
_AlaipmvVlanPort_ObjectIdentity=ObjectIdentity
alaipmvVlanPort=_AlaipmvVlanPort_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,1))
_AlaipmvVlanPortTable_Object=MibTable
alaipmvVlanPortTable=_AlaipmvVlanPortTable_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,1,1))
if mibBuilder.loadTexts:alaipmvVlanPortTable.setStatus(_A)
_AlaipmvVlanPortEntry_Object=MibTableRow
alaipmvVlanPortEntry=_AlaipmvVlanPortEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,1,1,1))
alaipmvVlanPortEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:alaipmvVlanPortEntry.setStatus(_A)
class _AlaipmvVlanPortIPMVlanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_AlaipmvVlanPortIPMVlanNumber_Type.__name__=_D
_AlaipmvVlanPortIPMVlanNumber_Object=MibTableColumn
alaipmvVlanPortIPMVlanNumber=_AlaipmvVlanPortIPMVlanNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,1,1,1,1),_AlaipmvVlanPortIPMVlanNumber_Type())
alaipmvVlanPortIPMVlanNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaipmvVlanPortIPMVlanNumber.setStatus(_A)
_AlaipmvVlanPortNumber_Type=InterfaceIndex
_AlaipmvVlanPortNumber_Object=MibTableColumn
alaipmvVlanPortNumber=_AlaipmvVlanPortNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,1,1,1,2),_AlaipmvVlanPortNumber_Type())
alaipmvVlanPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaipmvVlanPortNumber.setStatus(_A)
class _AlaipmvVlanPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('receiverPort',1),('senderPort',2)))
_AlaipmvVlanPortType_Type.__name__=_D
_AlaipmvVlanPortType_Object=MibTableColumn
alaipmvVlanPortType=_AlaipmvVlanPortType_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,1,1,1,3),_AlaipmvVlanPortType_Type())
alaipmvVlanPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaipmvVlanPortType.setStatus(_A)
_AlaipmvVlanPortRowStatus_Type=RowStatus
_AlaipmvVlanPortRowStatus_Object=MibTableColumn
alaipmvVlanPortRowStatus=_AlaipmvVlanPortRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,1,1,1,4),_AlaipmvVlanPortRowStatus_Type())
alaipmvVlanPortRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaipmvVlanPortRowStatus.setStatus(_A)
_AlaipmvVlanIpAddr_ObjectIdentity=ObjectIdentity
alaipmvVlanIpAddr=_AlaipmvVlanIpAddr_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,2))
_AlaipmvVlanIpAddrTable_Object=MibTable
alaipmvVlanIpAddrTable=_AlaipmvVlanIpAddrTable_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,2,1))
if mibBuilder.loadTexts:alaipmvVlanIpAddrTable.setStatus(_A)
_AlaipmvVlanIpAddrEntry_Object=MibTableRow
alaipmvVlanIpAddrEntry=_AlaipmvVlanIpAddrEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,2,1,1))
alaipmvVlanIpAddrEntry.setIndexNames((0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:alaipmvVlanIpAddrEntry.setStatus(_A)
class _AlaipmvVlanIpAddrVlanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_AlaipmvVlanIpAddrVlanNumber_Type.__name__=_D
_AlaipmvVlanIpAddrVlanNumber_Object=MibTableColumn
alaipmvVlanIpAddrVlanNumber=_AlaipmvVlanIpAddrVlanNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,2,1,1,1),_AlaipmvVlanIpAddrVlanNumber_Type())
alaipmvVlanIpAddrVlanNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaipmvVlanIpAddrVlanNumber.setStatus(_A)
class _AlaipmvVlanIpAddrType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AlaipmvVlanIpAddrType_Type.__name__=_H
_AlaipmvVlanIpAddrType_Object=MibTableColumn
alaipmvVlanIpAddrType=_AlaipmvVlanIpAddrType_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,2,1,1,2),_AlaipmvVlanIpAddrType_Type())
alaipmvVlanIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaipmvVlanIpAddrType.setStatus(_A)
class _AlaipmvVlanIpAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AlaipmvVlanIpAddress_Type.__name__=_G
_AlaipmvVlanIpAddress_Object=MibTableColumn
alaipmvVlanIpAddress=_AlaipmvVlanIpAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,2,1,1,3),_AlaipmvVlanIpAddress_Type())
alaipmvVlanIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alaipmvVlanIpAddress.setStatus(_A)
_AlaipmvVlanIpAddrRowStatus_Type=RowStatus
_AlaipmvVlanIpAddrRowStatus_Object=MibTableColumn
alaipmvVlanIpAddrRowStatus=_AlaipmvVlanIpAddrRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,2,1,1,4),_AlaipmvVlanIpAddrRowStatus_Type())
alaipmvVlanIpAddrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaipmvVlanIpAddrRowStatus.setStatus(_A)
_AlaipmvVlanIpAddrMaskTable_Object=MibTable
alaipmvVlanIpAddrMaskTable=_AlaipmvVlanIpAddrMaskTable_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,2,2))
if mibBuilder.loadTexts:alaipmvVlanIpAddrMaskTable.setStatus(_A)
_AlaipmvVlanIpAddrMaskEntry_Object=MibTableRow
alaipmvVlanIpAddrMaskEntry=_AlaipmvVlanIpAddrMaskEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,2,2,1))
alaipmvVlanIpAddrMaskEntry.setIndexNames((0,_B,_Q),(0,_B,_R),(0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:alaipmvVlanIpAddrMaskEntry.setStatus(_A)
class _AlaipmvVlanIpAddrMaskVlanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_AlaipmvVlanIpAddrMaskVlanNumber_Type.__name__=_D
_AlaipmvVlanIpAddrMaskVlanNumber_Object=MibTableColumn
alaipmvVlanIpAddrMaskVlanNumber=_AlaipmvVlanIpAddrMaskVlanNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,2,2,1,1),_AlaipmvVlanIpAddrMaskVlanNumber_Type())
alaipmvVlanIpAddrMaskVlanNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:alaipmvVlanIpAddrMaskVlanNumber.setStatus(_A)
class _AlaipmvVlanIpAddrMaskType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AlaipmvVlanIpAddrMaskType_Type.__name__=_H
_AlaipmvVlanIpAddrMaskType_Object=MibTableColumn
alaipmvVlanIpAddrMaskType=_AlaipmvVlanIpAddrMaskType_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,2,2,1,2),_AlaipmvVlanIpAddrMaskType_Type())
alaipmvVlanIpAddrMaskType.setMaxAccess(_F)
if mibBuilder.loadTexts:alaipmvVlanIpAddrMaskType.setStatus(_A)
class _AlaipmvVlanIpAddrMaskAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AlaipmvVlanIpAddrMaskAddress_Type.__name__=_G
_AlaipmvVlanIpAddrMaskAddress_Object=MibTableColumn
alaipmvVlanIpAddrMaskAddress=_AlaipmvVlanIpAddrMaskAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,2,2,1,3),_AlaipmvVlanIpAddrMaskAddress_Type())
alaipmvVlanIpAddrMaskAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:alaipmvVlanIpAddrMaskAddress.setStatus(_A)
_AlaipmvVlanIpAddrMaskPrefixLen_Type=InetAddressPrefixLength
_AlaipmvVlanIpAddrMaskPrefixLen_Object=MibTableColumn
alaipmvVlanIpAddrMaskPrefixLen=_AlaipmvVlanIpAddrMaskPrefixLen_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,2,2,1,4),_AlaipmvVlanIpAddrMaskPrefixLen_Type())
alaipmvVlanIpAddrMaskPrefixLen.setMaxAccess(_F)
if mibBuilder.loadTexts:alaipmvVlanIpAddrMaskPrefixLen.setStatus(_A)
_AlaipmvVlanIpAddrMaskRowStatus_Type=RowStatus
_AlaipmvVlanIpAddrMaskRowStatus_Object=MibTableColumn
alaipmvVlanIpAddrMaskRowStatus=_AlaipmvVlanIpAddrMaskRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,2,2,1,5),_AlaipmvVlanIpAddrMaskRowStatus_Type())
alaipmvVlanIpAddrMaskRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaipmvVlanIpAddrMaskRowStatus.setStatus(_A)
_AlaipmvVlanCtagT_ObjectIdentity=ObjectIdentity
alaipmvVlanCtagT=_AlaipmvVlanCtagT_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,3))
_AlaipmvVlanCtagTable_Object=MibTable
alaipmvVlanCtagTable=_AlaipmvVlanCtagTable_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,3,1))
if mibBuilder.loadTexts:alaipmvVlanCtagTable.setStatus(_A)
_AlaipmvVlanCtagEntry_Object=MibTableRow
alaipmvVlanCtagEntry=_AlaipmvVlanCtagEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,3,1,1))
alaipmvVlanCtagEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:alaipmvVlanCtagEntry.setStatus(_A)
class _AlaipmvVlanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_AlaipmvVlanNumber_Type.__name__=_D
_AlaipmvVlanNumber_Object=MibTableColumn
alaipmvVlanNumber=_AlaipmvVlanNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,3,1,1,1),_AlaipmvVlanNumber_Type())
alaipmvVlanNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaipmvVlanNumber.setStatus(_A)
class _AlaipmvVlanCtag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AlaipmvVlanCtag_Type.__name__=_D
_AlaipmvVlanCtag_Object=MibTableColumn
alaipmvVlanCtag=_AlaipmvVlanCtag_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,3,1,1,2),_AlaipmvVlanCtag_Type())
alaipmvVlanCtag.setMaxAccess(_C)
if mibBuilder.loadTexts:alaipmvVlanCtag.setStatus(_A)
_AlaipmvVlanCtagRowStatus_Type=RowStatus
_AlaipmvVlanCtagRowStatus_Object=MibTableColumn
alaipmvVlanCtagRowStatus=_AlaipmvVlanCtagRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,3,1,1,3),_AlaipmvVlanCtagRowStatus_Type())
alaipmvVlanCtagRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaipmvVlanCtagRowStatus.setStatus(_A)
_AlaipmvVlanIpAddrMask_ObjectIdentity=ObjectIdentity
alaipmvVlanIpAddrMask=_AlaipmvVlanIpAddrMask_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,4))
_AlaipmvReceiverVlanPort_ObjectIdentity=ObjectIdentity
alaipmvReceiverVlanPort=_AlaipmvReceiverVlanPort_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,5))
_AlaipmvReceiverVlanPortTable_Object=MibTable
alaipmvReceiverVlanPortTable=_AlaipmvReceiverVlanPortTable_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,5,1))
if mibBuilder.loadTexts:alaipmvReceiverVlanPortTable.setStatus(_A)
_AlaipmvReceiverVlanPortEntry_Object=MibTableRow
alaipmvReceiverVlanPortEntry=_AlaipmvReceiverVlanPortEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,5,1,1))
alaipmvReceiverVlanPortEntry.setIndexNames((0,_B,_U),(0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:alaipmvReceiverVlanPortEntry.setStatus(_A)
_AlaipmvReceiverVlanPortNumber_Type=InterfaceIndex
_AlaipmvReceiverVlanPortNumber_Object=MibTableColumn
alaipmvReceiverVlanPortNumber=_AlaipmvReceiverVlanPortNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,5,1,1,1),_AlaipmvReceiverVlanPortNumber_Type())
alaipmvReceiverVlanPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaipmvReceiverVlanPortNumber.setStatus(_A)
class _AlaipmvReceiverVlanPortIPMVlanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_AlaipmvReceiverVlanPortIPMVlanNumber_Type.__name__=_D
_AlaipmvReceiverVlanPortIPMVlanNumber_Object=MibTableColumn
alaipmvReceiverVlanPortIPMVlanNumber=_AlaipmvReceiverVlanPortIPMVlanNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,5,1,1,2),_AlaipmvReceiverVlanPortIPMVlanNumber_Type())
alaipmvReceiverVlanPortIPMVlanNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaipmvReceiverVlanPortIPMVlanNumber.setStatus(_A)
class _AlaipmvReceiverVlanPortRcvrVlanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_AlaipmvReceiverVlanPortRcvrVlanNumber_Type.__name__=_D
_AlaipmvReceiverVlanPortRcvrVlanNumber_Object=MibTableColumn
alaipmvReceiverVlanPortRcvrVlanNumber=_AlaipmvReceiverVlanPortRcvrVlanNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,5,1,1,3),_AlaipmvReceiverVlanPortRcvrVlanNumber_Type())
alaipmvReceiverVlanPortRcvrVlanNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaipmvReceiverVlanPortRcvrVlanNumber.setStatus(_A)
_AlaipmvReceiverVlanPortRowStatus_Type=RowStatus
_AlaipmvReceiverVlanPortRowStatus_Object=MibTableColumn
alaipmvReceiverVlanPortRowStatus=_AlaipmvReceiverVlanPortRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,41,1,1,5,1,1,4),_AlaipmvReceiverVlanPortRowStatus_Type())
alaipmvReceiverVlanPortRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaipmvReceiverVlanPortRowStatus.setStatus(_A)
_AlcatelIND1IPMVlanMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1IPMVlanMIBConformance=_AlcatelIND1IPMVlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,41,1,2))
if mibBuilder.loadTexts:alcatelIND1IPMVlanMIBConformance.setStatus(_A)
_AlcatelIND1IPMVlanMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1IPMVlanMIBGroups=_AlcatelIND1IPMVlanMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,41,1,2,1))
if mibBuilder.loadTexts:alcatelIND1IPMVlanMIBGroups.setStatus(_A)
_AlcatelIND1IPMVlanMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1IPMVlanMIBCompliances=_AlcatelIND1IPMVlanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,41,1,2,2))
if mibBuilder.loadTexts:alcatelIND1IPMVlanMIBCompliances.setStatus(_A)
alaipmvlanPortGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,41,1,2,1,1))
alaipmvlanPortGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_X)))
if mibBuilder.loadTexts:alaipmvlanPortGroup.setStatus(_A)
alaipmvlanIPAddressGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,41,1,2,1,2))
alaipmvlanIPAddressGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_Y)))
if mibBuilder.loadTexts:alaipmvlanIPAddressGroup.setStatus(_A)
alaipmvlanCtagGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,41,1,2,1,3))
alaipmvlanCtagGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Z)))
if mibBuilder.loadTexts:alaipmvlanCtagGroup.setStatus(_A)
alaipmvlanIPAddrMaskGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,41,1,2,1,4))
alaipmvlanIPAddrMaskGroup.setObjects((_B,_a))
if mibBuilder.loadTexts:alaipmvlanIPAddrMaskGroup.setStatus(_A)
alaipmReceiverVlanPortGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,41,1,2,1,5))
alaipmReceiverVlanPortGroup.setObjects((_B,_b))
if mibBuilder.loadTexts:alaipmReceiverVlanPortGroup.setStatus(_A)
alcatelIND1IPMVlanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,41,1,2,2,1))
alcatelIND1IPMVlanMIBCompliance.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:alcatelIND1IPMVlanMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1IPMVlanMIB':alcatelIND1IPMVlanMIB,'alcatelIND1IPMVlanMIBObjects':alcatelIND1IPMVlanMIBObjects,'alaipmvVlanPort':alaipmvVlanPort,'alaipmvVlanPortTable':alaipmvVlanPortTable,'alaipmvVlanPortEntry':alaipmvVlanPortEntry,_I:alaipmvVlanPortIPMVlanNumber,_J:alaipmvVlanPortNumber,_K:alaipmvVlanPortType,_X:alaipmvVlanPortRowStatus,'alaipmvVlanIpAddr':alaipmvVlanIpAddr,'alaipmvVlanIpAddrTable':alaipmvVlanIpAddrTable,'alaipmvVlanIpAddrEntry':alaipmvVlanIpAddrEntry,_L:alaipmvVlanIpAddrVlanNumber,_M:alaipmvVlanIpAddrType,_N:alaipmvVlanIpAddress,_Y:alaipmvVlanIpAddrRowStatus,'alaipmvVlanIpAddrMaskTable':alaipmvVlanIpAddrMaskTable,'alaipmvVlanIpAddrMaskEntry':alaipmvVlanIpAddrMaskEntry,_Q:alaipmvVlanIpAddrMaskVlanNumber,_R:alaipmvVlanIpAddrMaskType,_S:alaipmvVlanIpAddrMaskAddress,_T:alaipmvVlanIpAddrMaskPrefixLen,_a:alaipmvVlanIpAddrMaskRowStatus,'alaipmvVlanCtagT':alaipmvVlanCtagT,'alaipmvVlanCtagTable':alaipmvVlanCtagTable,'alaipmvVlanCtagEntry':alaipmvVlanCtagEntry,_O:alaipmvVlanNumber,_P:alaipmvVlanCtag,_Z:alaipmvVlanCtagRowStatus,'alaipmvVlanIpAddrMask':alaipmvVlanIpAddrMask,'alaipmvReceiverVlanPort':alaipmvReceiverVlanPort,'alaipmvReceiverVlanPortTable':alaipmvReceiverVlanPortTable,'alaipmvReceiverVlanPortEntry':alaipmvReceiverVlanPortEntry,_U:alaipmvReceiverVlanPortNumber,_V:alaipmvReceiverVlanPortIPMVlanNumber,_W:alaipmvReceiverVlanPortRcvrVlanNumber,_b:alaipmvReceiverVlanPortRowStatus,'alcatelIND1IPMVlanMIBConformance':alcatelIND1IPMVlanMIBConformance,'alcatelIND1IPMVlanMIBGroups':alcatelIND1IPMVlanMIBGroups,_c:alaipmvlanPortGroup,_d:alaipmvlanIPAddressGroup,_f:alaipmvlanCtagGroup,_e:alaipmvlanIPAddrMaskGroup,_g:alaipmReceiverVlanPortGroup,'alcatelIND1IPMVlanMIBCompliances':alcatelIND1IPMVlanMIBCompliances,'alcatelIND1IPMVlanMIBCompliance':alcatelIND1IPMVlanMIBCompliance})