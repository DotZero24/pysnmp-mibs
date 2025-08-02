_R='ctbrDevIfConfigGroup'
_Q='ctbrMSDUMaxLength'
_P='ctbrIpMask'
_O='ctbrIpMaskType'
_N='ctbrIpAddress'
_M='ctbrIpAddressType'
_L='ctbrDefaultIpMask'
_K='ctbrDefaultIpMaskType'
_J='ctbrDefaultIpAddress'
_I='ctbrDefaultIpAddrType'
_H='ctbrPhyAddress'
_G='ctbrDefaultPhyAddress'
_F='read-only'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='CISCO-TBRIDGE-DEV-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_D,_E)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
ciscoTBridgeDevIfMIB=ModuleIdentity((1,3,6,1,4,1,9,9,269))
if mibBuilder.loadTexts:ciscoTBridgeDevIfMIB.setRevisions(('2002-04-03 00:01',))
_CiscoTBridgeDevIfMIBObjects_ObjectIdentity=ObjectIdentity
ciscoTBridgeDevIfMIBObjects=_CiscoTBridgeDevIfMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,269,1))
_CtbrDevInterface_ObjectIdentity=ObjectIdentity
ctbrDevInterface=_CtbrDevInterface_ObjectIdentity((1,3,6,1,4,1,9,9,269,1,1))
_CtbrDevInterfaceTable_Object=MibTable
ctbrDevInterfaceTable=_CtbrDevInterfaceTable_Object((1,3,6,1,4,1,9,9,269,1,1,1))
if mibBuilder.loadTexts:ctbrDevInterfaceTable.setStatus(_A)
_CtbrDevInterfaceEntry_Object=MibTableRow
ctbrDevInterfaceEntry=_CtbrDevInterfaceEntry_Object((1,3,6,1,4,1,9,9,269,1,1,1,1))
ctbrDevInterfaceEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ctbrDevInterfaceEntry.setStatus(_A)
_CtbrDefaultPhyAddress_Type=MacAddress
_CtbrDefaultPhyAddress_Object=MibTableColumn
ctbrDefaultPhyAddress=_CtbrDefaultPhyAddress_Object((1,3,6,1,4,1,9,9,269,1,1,1,1,1),_CtbrDefaultPhyAddress_Type())
ctbrDefaultPhyAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:ctbrDefaultPhyAddress.setStatus(_A)
_CtbrPhyAddress_Type=MacAddress
_CtbrPhyAddress_Object=MibTableColumn
ctbrPhyAddress=_CtbrPhyAddress_Object((1,3,6,1,4,1,9,9,269,1,1,1,1,2),_CtbrPhyAddress_Type())
ctbrPhyAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctbrPhyAddress.setStatus(_A)
_CtbrDefaultIpAddrType_Type=InetAddressType
_CtbrDefaultIpAddrType_Object=MibTableColumn
ctbrDefaultIpAddrType=_CtbrDefaultIpAddrType_Object((1,3,6,1,4,1,9,9,269,1,1,1,1,3),_CtbrDefaultIpAddrType_Type())
ctbrDefaultIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctbrDefaultIpAddrType.setStatus(_A)
_CtbrDefaultIpAddress_Type=InetAddress
_CtbrDefaultIpAddress_Object=MibTableColumn
ctbrDefaultIpAddress=_CtbrDefaultIpAddress_Object((1,3,6,1,4,1,9,9,269,1,1,1,1,4),_CtbrDefaultIpAddress_Type())
ctbrDefaultIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctbrDefaultIpAddress.setStatus(_A)
_CtbrDefaultIpMaskType_Type=InetAddressType
_CtbrDefaultIpMaskType_Object=MibTableColumn
ctbrDefaultIpMaskType=_CtbrDefaultIpMaskType_Object((1,3,6,1,4,1,9,9,269,1,1,1,1,5),_CtbrDefaultIpMaskType_Type())
ctbrDefaultIpMaskType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctbrDefaultIpMaskType.setStatus(_A)
_CtbrDefaultIpMask_Type=InetAddress
_CtbrDefaultIpMask_Object=MibTableColumn
ctbrDefaultIpMask=_CtbrDefaultIpMask_Object((1,3,6,1,4,1,9,9,269,1,1,1,1,6),_CtbrDefaultIpMask_Type())
ctbrDefaultIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ctbrDefaultIpMask.setStatus(_A)
_CtbrIpAddressType_Type=InetAddressType
_CtbrIpAddressType_Object=MibTableColumn
ctbrIpAddressType=_CtbrIpAddressType_Object((1,3,6,1,4,1,9,9,269,1,1,1,1,7),_CtbrIpAddressType_Type())
ctbrIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctbrIpAddressType.setStatus(_A)
_CtbrIpAddress_Type=InetAddress
_CtbrIpAddress_Object=MibTableColumn
ctbrIpAddress=_CtbrIpAddress_Object((1,3,6,1,4,1,9,9,269,1,1,1,1,8),_CtbrIpAddress_Type())
ctbrIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctbrIpAddress.setStatus(_A)
_CtbrIpMaskType_Type=InetAddressType
_CtbrIpMaskType_Object=MibTableColumn
ctbrIpMaskType=_CtbrIpMaskType_Object((1,3,6,1,4,1,9,9,269,1,1,1,1,9),_CtbrIpMaskType_Type())
ctbrIpMaskType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctbrIpMaskType.setStatus(_A)
_CtbrIpMask_Type=InetAddress
_CtbrIpMask_Object=MibTableColumn
ctbrIpMask=_CtbrIpMask_Object((1,3,6,1,4,1,9,9,269,1,1,1,1,10),_CtbrIpMask_Type())
ctbrIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ctbrIpMask.setStatus(_A)
_CtbrMSDUMaxLength_Type=Unsigned32
_CtbrMSDUMaxLength_Object=MibTableColumn
ctbrMSDUMaxLength=_CtbrMSDUMaxLength_Object((1,3,6,1,4,1,9,9,269,1,1,1,1,11),_CtbrMSDUMaxLength_Type())
ctbrMSDUMaxLength.setMaxAccess(_F)
if mibBuilder.loadTexts:ctbrMSDUMaxLength.setStatus(_A)
_CiscoTBridgeDevIfMIBConformance_ObjectIdentity=ObjectIdentity
ciscoTBridgeDevIfMIBConformance=_CiscoTBridgeDevIfMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,269,2))
_CiscoTBridgeDevIfMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoTBridgeDevIfMIBCompliances=_CiscoTBridgeDevIfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,269,2,1))
_CiscoTBridgeDevIfMIBGroups_ObjectIdentity=ObjectIdentity
ciscoTBridgeDevIfMIBGroups=_CiscoTBridgeDevIfMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,269,2,2))
ctbrDevIfConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,269,2,2,1))
ctbrDevIfConfigGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ctbrDevIfConfigGroup.setStatus(_A)
ciscoTBridgeDevIfCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,269,2,1,1))
ciscoTBridgeDevIfCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:ciscoTBridgeDevIfCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoTBridgeDevIfMIB':ciscoTBridgeDevIfMIB,'ciscoTBridgeDevIfMIBObjects':ciscoTBridgeDevIfMIBObjects,'ctbrDevInterface':ctbrDevInterface,'ctbrDevInterfaceTable':ctbrDevInterfaceTable,'ctbrDevInterfaceEntry':ctbrDevInterfaceEntry,_G:ctbrDefaultPhyAddress,_H:ctbrPhyAddress,_I:ctbrDefaultIpAddrType,_J:ctbrDefaultIpAddress,_K:ctbrDefaultIpMaskType,_L:ctbrDefaultIpMask,_M:ctbrIpAddressType,_N:ctbrIpAddress,_O:ctbrIpMaskType,_P:ctbrIpMask,_Q:ctbrMSDUMaxLength,'ciscoTBridgeDevIfMIBConformance':ciscoTBridgeDevIfMIBConformance,'ciscoTBridgeDevIfMIBCompliances':ciscoTBridgeDevIfMIBCompliances,'ciscoTBridgeDevIfCompliance':ciscoTBridgeDevIfCompliance,'ciscoTBridgeDevIfMIBGroups':ciscoTBridgeDevIfMIBGroups,_R:ctbrDevIfConfigGroup})