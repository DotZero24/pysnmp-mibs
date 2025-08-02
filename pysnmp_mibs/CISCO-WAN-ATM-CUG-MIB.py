_T='ciscoWanAtmAddressCugGroup'
_S='ciscoWanAtmCugGroup'
_R='cwaPreferentialCug'
_Q='cwaOutgoingAccess'
_P='cwaIncomingAccess'
_O='cwaCugAtmAddressPlan'
_N='cwaCugRowStatus'
_M='cwaCallsBarred'
_L='cwaInterlockCode'
_K='cwaAddressPlan'
_J='notAllowed'
_I='cwaCugIndex'
_H='not-accessible'
_G='cwaAddressLength'
_F='cwaAtmAddress'
_E='read-write'
_D='read-create'
_C='Integer32'
_B='CISCO-WAN-ATM-CUG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmAddr,=mibBuilder.importSymbols('ATM-TC-MIB','AtmAddr')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoWanAtmCugMIB=ModuleIdentity((1,3,6,1,4,1,9,9,99999))
if mibBuilder.loadTexts:ciscoWanAtmCugMIB.setRevisions(('2002-03-22 00:00',))
class CiscoAtmAddressType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,8)));namedValues=NamedValues(*(('e164',3),('nsap',8)))
class CiscoAtmAddressLength(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,160))
class CiscoAtmInterlockCode(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(24,24));fixedLength=24
_CwaCugMIBNotifications_ObjectIdentity=ObjectIdentity
cwaCugMIBNotifications=_CwaCugMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,99999,0))
_CwaCugMIBObjects_ObjectIdentity=ObjectIdentity
cwaCugMIBObjects=_CwaCugMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,99999,1))
_CwaCug_ObjectIdentity=ObjectIdentity
cwaCug=_CwaCug_ObjectIdentity((1,3,6,1,4,1,9,9,99999,1,1))
_CwaCugTable_Object=MibTable
cwaCugTable=_CwaCugTable_Object((1,3,6,1,4,1,9,9,99999,1,1,1))
if mibBuilder.loadTexts:cwaCugTable.setStatus(_A)
_CwaCugEntry_Object=MibTableRow
cwaCugEntry=_CwaCugEntry_Object((1,3,6,1,4,1,9,9,99999,1,1,1,1))
cwaCugEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_I))
if mibBuilder.loadTexts:cwaCugEntry.setStatus(_A)
_CwaAtmAddress_Type=AtmAddr
_CwaAtmAddress_Object=MibTableColumn
cwaAtmAddress=_CwaAtmAddress_Object((1,3,6,1,4,1,9,9,99999,1,1,1,1,1),_CwaAtmAddress_Type())
cwaAtmAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:cwaAtmAddress.setStatus(_A)
_CwaAddressLength_Type=CiscoAtmAddressLength
_CwaAddressLength_Object=MibTableColumn
cwaAddressLength=_CwaAddressLength_Object((1,3,6,1,4,1,9,9,99999,1,1,1,1,2),_CwaAddressLength_Type())
cwaAddressLength.setMaxAccess(_H)
if mibBuilder.loadTexts:cwaAddressLength.setStatus(_A)
class _CwaCugIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CwaCugIndex_Type.__name__=_C
_CwaCugIndex_Object=MibTableColumn
cwaCugIndex=_CwaCugIndex_Object((1,3,6,1,4,1,9,9,99999,1,1,1,1,3),_CwaCugIndex_Type())
cwaCugIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cwaCugIndex.setStatus(_A)
_CwaAddressPlan_Type=CiscoAtmAddressType
_CwaAddressPlan_Object=MibTableColumn
cwaAddressPlan=_CwaAddressPlan_Object((1,3,6,1,4,1,9,9,99999,1,1,1,1,4),_CwaAddressPlan_Type())
cwaAddressPlan.setMaxAccess(_D)
if mibBuilder.loadTexts:cwaAddressPlan.setStatus(_A)
_CwaInterlockCode_Type=CiscoAtmInterlockCode
_CwaInterlockCode_Object=MibTableColumn
cwaInterlockCode=_CwaInterlockCode_Object((1,3,6,1,4,1,9,9,99999,1,1,1,1,5),_CwaInterlockCode_Type())
cwaInterlockCode.setMaxAccess(_D)
if mibBuilder.loadTexts:cwaInterlockCode.setStatus(_A)
class _CwaCallsBarred_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('incoming',2),('outgoing',3)))
_CwaCallsBarred_Type.__name__=_C
_CwaCallsBarred_Object=MibTableColumn
cwaCallsBarred=_CwaCallsBarred_Object((1,3,6,1,4,1,9,9,99999,1,1,1,1,6),_CwaCallsBarred_Type())
cwaCallsBarred.setMaxAccess(_D)
if mibBuilder.loadTexts:cwaCallsBarred.setStatus(_A)
_CwaCugRowStatus_Type=RowStatus
_CwaCugRowStatus_Object=MibTableColumn
cwaCugRowStatus=_CwaCugRowStatus_Object((1,3,6,1,4,1,9,9,99999,1,1,1,1,7),_CwaCugRowStatus_Type())
cwaCugRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cwaCugRowStatus.setStatus(_A)
_CwaAddressCug_ObjectIdentity=ObjectIdentity
cwaAddressCug=_CwaAddressCug_ObjectIdentity((1,3,6,1,4,1,9,9,99999,1,2))
_CwaAddressCugTable_Object=MibTable
cwaAddressCugTable=_CwaAddressCugTable_Object((1,3,6,1,4,1,9,9,99999,1,2,1))
if mibBuilder.loadTexts:cwaAddressCugTable.setStatus(_A)
_CwaAddressCugEntry_Object=MibTableRow
cwaAddressCugEntry=_CwaAddressCugEntry_Object((1,3,6,1,4,1,9,9,99999,1,2,1,1))
cwaAddressCugEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:cwaAddressCugEntry.setStatus(_A)
_CwaCugAtmAddressPlan_Type=CiscoAtmAddressType
_CwaCugAtmAddressPlan_Object=MibTableColumn
cwaCugAtmAddressPlan=_CwaCugAtmAddressPlan_Object((1,3,6,1,4,1,9,9,99999,1,2,1,1,1),_CwaCugAtmAddressPlan_Type())
cwaCugAtmAddressPlan.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaCugAtmAddressPlan.setStatus(_A)
class _CwaIncomingAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('allowed',2)))
_CwaIncomingAccess_Type.__name__=_C
_CwaIncomingAccess_Object=MibTableColumn
cwaIncomingAccess=_CwaIncomingAccess_Object((1,3,6,1,4,1,9,9,99999,1,2,1,1,2),_CwaIncomingAccess_Type())
cwaIncomingAccess.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaIncomingAccess.setStatus(_A)
class _CwaOutgoingAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('allowedPerCall',2),('allowedPermanently',3)))
_CwaOutgoingAccess_Type.__name__=_C
_CwaOutgoingAccess_Object=MibTableColumn
cwaOutgoingAccess=_CwaOutgoingAccess_Object((1,3,6,1,4,1,9,9,99999,1,2,1,1,3),_CwaOutgoingAccess_Type())
cwaOutgoingAccess.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaOutgoingAccess.setStatus(_A)
class _CwaPreferentialCug_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwaPreferentialCug_Type.__name__=_C
_CwaPreferentialCug_Object=MibTableColumn
cwaPreferentialCug=_CwaPreferentialCug_Object((1,3,6,1,4,1,9,9,99999,1,2,1,1,4),_CwaPreferentialCug_Type())
cwaPreferentialCug.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaPreferentialCug.setStatus(_A)
_CiscoWanAtmCugMIBConformance_ObjectIdentity=ObjectIdentity
ciscoWanAtmCugMIBConformance=_CiscoWanAtmCugMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,99999,3))
_CiscoWanAtmCugMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWanAtmCugMIBCompliances=_CiscoWanAtmCugMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,99999,3,1))
_CiscoWanAtmCugMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWanAtmCugMIBGroups=_CiscoWanAtmCugMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,99999,3,2))
ciscoWanAtmCugGroup=ObjectGroup((1,3,6,1,4,1,9,9,99999,3,2,1))
ciscoWanAtmCugGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ciscoWanAtmCugGroup.setStatus(_A)
ciscoWanAtmAddressCugGroup=ObjectGroup((1,3,6,1,4,1,9,9,99999,3,2,2))
ciscoWanAtmAddressCugGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ciscoWanAtmAddressCugGroup.setStatus(_A)
ciscoWanAtmCugMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,99999,3,1,1))
ciscoWanAtmCugMIBCompliance.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ciscoWanAtmCugMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CiscoAtmAddressType':CiscoAtmAddressType,'CiscoAtmAddressLength':CiscoAtmAddressLength,'CiscoAtmInterlockCode':CiscoAtmInterlockCode,'ciscoWanAtmCugMIB':ciscoWanAtmCugMIB,'cwaCugMIBNotifications':cwaCugMIBNotifications,'cwaCugMIBObjects':cwaCugMIBObjects,'cwaCug':cwaCug,'cwaCugTable':cwaCugTable,'cwaCugEntry':cwaCugEntry,_F:cwaAtmAddress,_G:cwaAddressLength,_I:cwaCugIndex,_K:cwaAddressPlan,_L:cwaInterlockCode,_M:cwaCallsBarred,_N:cwaCugRowStatus,'cwaAddressCug':cwaAddressCug,'cwaAddressCugTable':cwaAddressCugTable,'cwaAddressCugEntry':cwaAddressCugEntry,_O:cwaCugAtmAddressPlan,_P:cwaIncomingAccess,_Q:cwaOutgoingAccess,_R:cwaPreferentialCug,'ciscoWanAtmCugMIBConformance':ciscoWanAtmCugMIBConformance,'ciscoWanAtmCugMIBCompliances':ciscoWanAtmCugMIBCompliances,'ciscoWanAtmCugMIBCompliance':ciscoWanAtmCugMIBCompliance,'ciscoWanAtmCugMIBGroups':ciscoWanAtmCugMIBGroups,_S:ciscoWanAtmCugGroup,_T:ciscoWanAtmAddressCugGroup})