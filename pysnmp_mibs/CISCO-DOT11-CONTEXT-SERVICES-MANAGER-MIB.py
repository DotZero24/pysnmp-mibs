_M='ciscoDot11CsMgrClientGroup'
_L='cDot11CsMgrClntStateTransitions'
_K='cDot11CsMgrClntRegistLifeTime'
_J='cDot11CsMgrClntOperMode'
_I='cDot11CsMgrClntMnAuthenAddr'
_H='cDot11CsMgrClntRootNodeAddr'
_G='cDot11CsMgrClntParentWdsAddr'
_F='cDot11CsMgrClntAddressType'
_E='cDot11CsMgrClntModuleIndex'
_D='Integer32'
_C='read-only'
_B='CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeInterval')
ciscoDot11CsMgrMIB=ModuleIdentity((1,3,6,1,4,1,9,9,3228))
if mibBuilder.loadTexts:ciscoDot11CsMgrMIB.setRevisions(('2003-11-02 00:00',))
class Cdot11CsModuleIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CiscoDot11CsMgrMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDot11CsMgrMIBObjects=_CiscoDot11CsMgrMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,3228,1))
_CiscoDot11CsMgrClientConfig_ObjectIdentity=ObjectIdentity
ciscoDot11CsMgrClientConfig=_CiscoDot11CsMgrClientConfig_ObjectIdentity((1,3,6,1,4,1,9,9,3228,1,1))
_CDot11CsMgrClientTable_Object=MibTable
cDot11CsMgrClientTable=_CDot11CsMgrClientTable_Object((1,3,6,1,4,1,9,9,3228,1,1,1))
if mibBuilder.loadTexts:cDot11CsMgrClientTable.setStatus(_A)
_CDot11CsMgrClientEntry_Object=MibTableRow
cDot11CsMgrClientEntry=_CDot11CsMgrClientEntry_Object((1,3,6,1,4,1,9,9,3228,1,1,1,1))
cDot11CsMgrClientEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cDot11CsMgrClientEntry.setStatus(_A)
_CDot11CsMgrClntModuleIndex_Type=Cdot11CsModuleIndex
_CDot11CsMgrClntModuleIndex_Object=MibTableColumn
cDot11CsMgrClntModuleIndex=_CDot11CsMgrClntModuleIndex_Object((1,3,6,1,4,1,9,9,3228,1,1,1,1,1),_CDot11CsMgrClntModuleIndex_Type())
cDot11CsMgrClntModuleIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cDot11CsMgrClntModuleIndex.setStatus(_A)
_CDot11CsMgrClntAddressType_Type=InetAddressType
_CDot11CsMgrClntAddressType_Object=MibTableColumn
cDot11CsMgrClntAddressType=_CDot11CsMgrClntAddressType_Object((1,3,6,1,4,1,9,9,3228,1,1,1,1,2),_CDot11CsMgrClntAddressType_Type())
cDot11CsMgrClntAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11CsMgrClntAddressType.setStatus(_A)
_CDot11CsMgrClntParentWdsAddr_Type=InetAddress
_CDot11CsMgrClntParentWdsAddr_Object=MibTableColumn
cDot11CsMgrClntParentWdsAddr=_CDot11CsMgrClntParentWdsAddr_Object((1,3,6,1,4,1,9,9,3228,1,1,1,1,3),_CDot11CsMgrClntParentWdsAddr_Type())
cDot11CsMgrClntParentWdsAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11CsMgrClntParentWdsAddr.setStatus(_A)
_CDot11CsMgrClntRootNodeAddr_Type=InetAddress
_CDot11CsMgrClntRootNodeAddr_Object=MibTableColumn
cDot11CsMgrClntRootNodeAddr=_CDot11CsMgrClntRootNodeAddr_Object((1,3,6,1,4,1,9,9,3228,1,1,1,1,4),_CDot11CsMgrClntRootNodeAddr_Type())
cDot11CsMgrClntRootNodeAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11CsMgrClntRootNodeAddr.setStatus(_A)
_CDot11CsMgrClntMnAuthenAddr_Type=InetAddress
_CDot11CsMgrClntMnAuthenAddr_Object=MibTableColumn
cDot11CsMgrClntMnAuthenAddr=_CDot11CsMgrClntMnAuthenAddr_Object((1,3,6,1,4,1,9,9,3228,1,1,1,1,5),_CDot11CsMgrClntMnAuthenAddr_Type())
cDot11CsMgrClntMnAuthenAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11CsMgrClntMnAuthenAddr.setStatus(_A)
class _CDot11CsMgrClntOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('infrastructure',1),('distributed',2)))
_CDot11CsMgrClntOperMode_Type.__name__=_D
_CDot11CsMgrClntOperMode_Object=MibTableColumn
cDot11CsMgrClntOperMode=_CDot11CsMgrClntOperMode_Object((1,3,6,1,4,1,9,9,3228,1,1,1,1,6),_CDot11CsMgrClntOperMode_Type())
cDot11CsMgrClntOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11CsMgrClntOperMode.setStatus(_A)
_CDot11CsMgrClntRegistLifeTime_Type=TimeInterval
_CDot11CsMgrClntRegistLifeTime_Object=MibTableColumn
cDot11CsMgrClntRegistLifeTime=_CDot11CsMgrClntRegistLifeTime_Object((1,3,6,1,4,1,9,9,3228,1,1,1,1,7),_CDot11CsMgrClntRegistLifeTime_Type())
cDot11CsMgrClntRegistLifeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11CsMgrClntRegistLifeTime.setStatus(_A)
_CDot11CsMgrClntStateTransitions_Type=Counter32
_CDot11CsMgrClntStateTransitions_Object=MibTableColumn
cDot11CsMgrClntStateTransitions=_CDot11CsMgrClntStateTransitions_Object((1,3,6,1,4,1,9,9,3228,1,1,1,1,8),_CDot11CsMgrClntStateTransitions_Type())
cDot11CsMgrClntStateTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11CsMgrClntStateTransitions.setStatus(_A)
_CiscoDot11CsMgrMIBConformance_ObjectIdentity=ObjectIdentity
ciscoDot11CsMgrMIBConformance=_CiscoDot11CsMgrMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,3228,2))
_CiscoDot11CsMgrMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDot11CsMgrMIBCompliances=_CiscoDot11CsMgrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,3228,2,1))
_CiscoDot11CsMgrMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDot11CsMgrMIBGroups=_CiscoDot11CsMgrMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,3228,2,2))
ciscoDot11CsMgrClientGroup=ObjectGroup((1,3,6,1,4,1,9,9,3228,2,2,1))
ciscoDot11CsMgrClientGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:ciscoDot11CsMgrClientGroup.setStatus(_A)
ciscoDot11CsMgrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,3228,2,1,1))
ciscoDot11CsMgrMIBCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:ciscoDot11CsMgrMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Cdot11CsModuleIndex':Cdot11CsModuleIndex,'ciscoDot11CsMgrMIB':ciscoDot11CsMgrMIB,'ciscoDot11CsMgrMIBObjects':ciscoDot11CsMgrMIBObjects,'ciscoDot11CsMgrClientConfig':ciscoDot11CsMgrClientConfig,'cDot11CsMgrClientTable':cDot11CsMgrClientTable,'cDot11CsMgrClientEntry':cDot11CsMgrClientEntry,_E:cDot11CsMgrClntModuleIndex,_F:cDot11CsMgrClntAddressType,_G:cDot11CsMgrClntParentWdsAddr,_H:cDot11CsMgrClntRootNodeAddr,_I:cDot11CsMgrClntMnAuthenAddr,_J:cDot11CsMgrClntOperMode,_K:cDot11CsMgrClntRegistLifeTime,_L:cDot11CsMgrClntStateTransitions,'ciscoDot11CsMgrMIBConformance':ciscoDot11CsMgrMIBConformance,'ciscoDot11CsMgrMIBCompliances':ciscoDot11CsMgrMIBCompliances,'ciscoDot11CsMgrMIBCompliance':ciscoDot11CsMgrMIBCompliance,'ciscoDot11CsMgrMIBGroups':ciscoDot11CsMgrMIBGroups,_M:ciscoDot11CsMgrClientGroup})