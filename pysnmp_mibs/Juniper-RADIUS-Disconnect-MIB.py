_W='juniRadiusDisconnectGroup'
_V='juniRadiusDisconnectCfgRowStatus'
_U='juniRadiusDisconnectCfgKey'
_T='juniRadiusDisconnectCfgClientPortNumber'
_S='juniRadiusDisconnectPacketsDropped'
_R='juniRadiusDisconnectUnknownTypes'
_Q='juniRadiusDisconnectBadAuthenticators'
_P='juniRadiusDisconnectNoSessionIds'
_O='juniRadiusDisconnectNoSecret'
_N='juniRadiusDisconnectRejects'
_M='juniRadiusDisconnectAccepts'
_L='juniRadiusDisconnectRequests'
_K='juniRadiusDisconnectClientPortNumber'
_J='juniRadiusDisconnectInvalidClientAddresses'
_I='juniRadiusDisconnectCfgClientAddress'
_H='not-accessible'
_G='juniRadiusDisconnectClientAddress'
_F='DisplayString'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='Juniper-RADIUS-Disconnect-MIB'
_A='obsolete'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
juniRadiusDisconnectMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,67))
if mibBuilder.loadTexts:juniRadiusDisconnectMIB.setRevisions(('2004-06-09 13:57','2003-01-13 20:50'))
_JuniRadiusDisconnectObjects_ObjectIdentity=ObjectIdentity
juniRadiusDisconnectObjects=_JuniRadiusDisconnectObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,67,1))
_JuniRadiusDisconnect_ObjectIdentity=ObjectIdentity
juniRadiusDisconnect=_JuniRadiusDisconnect_ObjectIdentity((1,3,6,1,4,1,4874,2,2,67,1,1))
_JuniRadiusDisconnectInvalidClientAddresses_Type=Counter32
_JuniRadiusDisconnectInvalidClientAddresses_Object=MibScalar
juniRadiusDisconnectInvalidClientAddresses=_JuniRadiusDisconnectInvalidClientAddresses_Object((1,3,6,1,4,1,4874,2,2,67,1,1,1),_JuniRadiusDisconnectInvalidClientAddresses_Type())
juniRadiusDisconnectInvalidClientAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRadiusDisconnectInvalidClientAddresses.setStatus(_A)
_JuniRadiusDisconnectClientTable_Object=MibTable
juniRadiusDisconnectClientTable=_JuniRadiusDisconnectClientTable_Object((1,3,6,1,4,1,4874,2,2,67,1,1,2))
if mibBuilder.loadTexts:juniRadiusDisconnectClientTable.setStatus(_A)
_JuniRadiusDisconnectClientEntry_Object=MibTableRow
juniRadiusDisconnectClientEntry=_JuniRadiusDisconnectClientEntry_Object((1,3,6,1,4,1,4874,2,2,67,1,1,2,1))
juniRadiusDisconnectClientEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:juniRadiusDisconnectClientEntry.setStatus(_A)
_JuniRadiusDisconnectClientAddress_Type=IpAddress
_JuniRadiusDisconnectClientAddress_Object=MibTableColumn
juniRadiusDisconnectClientAddress=_JuniRadiusDisconnectClientAddress_Object((1,3,6,1,4,1,4874,2,2,67,1,1,2,1,1),_JuniRadiusDisconnectClientAddress_Type())
juniRadiusDisconnectClientAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:juniRadiusDisconnectClientAddress.setStatus(_A)
_JuniRadiusDisconnectClientPortNumber_Type=Integer32
_JuniRadiusDisconnectClientPortNumber_Object=MibTableColumn
juniRadiusDisconnectClientPortNumber=_JuniRadiusDisconnectClientPortNumber_Object((1,3,6,1,4,1,4874,2,2,67,1,1,2,1,2),_JuniRadiusDisconnectClientPortNumber_Type())
juniRadiusDisconnectClientPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRadiusDisconnectClientPortNumber.setStatus(_A)
_JuniRadiusDisconnectRequests_Type=Counter32
_JuniRadiusDisconnectRequests_Object=MibTableColumn
juniRadiusDisconnectRequests=_JuniRadiusDisconnectRequests_Object((1,3,6,1,4,1,4874,2,2,67,1,1,2,1,3),_JuniRadiusDisconnectRequests_Type())
juniRadiusDisconnectRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRadiusDisconnectRequests.setStatus(_A)
_JuniRadiusDisconnectAccepts_Type=Counter32
_JuniRadiusDisconnectAccepts_Object=MibTableColumn
juniRadiusDisconnectAccepts=_JuniRadiusDisconnectAccepts_Object((1,3,6,1,4,1,4874,2,2,67,1,1,2,1,4),_JuniRadiusDisconnectAccepts_Type())
juniRadiusDisconnectAccepts.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRadiusDisconnectAccepts.setStatus(_A)
_JuniRadiusDisconnectRejects_Type=Counter32
_JuniRadiusDisconnectRejects_Object=MibTableColumn
juniRadiusDisconnectRejects=_JuniRadiusDisconnectRejects_Object((1,3,6,1,4,1,4874,2,2,67,1,1,2,1,5),_JuniRadiusDisconnectRejects_Type())
juniRadiusDisconnectRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRadiusDisconnectRejects.setStatus(_A)
_JuniRadiusDisconnectNoSecret_Type=Counter32
_JuniRadiusDisconnectNoSecret_Object=MibTableColumn
juniRadiusDisconnectNoSecret=_JuniRadiusDisconnectNoSecret_Object((1,3,6,1,4,1,4874,2,2,67,1,1,2,1,6),_JuniRadiusDisconnectNoSecret_Type())
juniRadiusDisconnectNoSecret.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRadiusDisconnectNoSecret.setStatus(_A)
_JuniRadiusDisconnectNoSessionIds_Type=Counter32
_JuniRadiusDisconnectNoSessionIds_Object=MibTableColumn
juniRadiusDisconnectNoSessionIds=_JuniRadiusDisconnectNoSessionIds_Object((1,3,6,1,4,1,4874,2,2,67,1,1,2,1,7),_JuniRadiusDisconnectNoSessionIds_Type())
juniRadiusDisconnectNoSessionIds.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRadiusDisconnectNoSessionIds.setStatus(_A)
_JuniRadiusDisconnectBadAuthenticators_Type=Counter32
_JuniRadiusDisconnectBadAuthenticators_Object=MibTableColumn
juniRadiusDisconnectBadAuthenticators=_JuniRadiusDisconnectBadAuthenticators_Object((1,3,6,1,4,1,4874,2,2,67,1,1,2,1,8),_JuniRadiusDisconnectBadAuthenticators_Type())
juniRadiusDisconnectBadAuthenticators.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRadiusDisconnectBadAuthenticators.setStatus(_A)
_JuniRadiusDisconnectUnknownTypes_Type=Counter32
_JuniRadiusDisconnectUnknownTypes_Object=MibTableColumn
juniRadiusDisconnectUnknownTypes=_JuniRadiusDisconnectUnknownTypes_Object((1,3,6,1,4,1,4874,2,2,67,1,1,2,1,9),_JuniRadiusDisconnectUnknownTypes_Type())
juniRadiusDisconnectUnknownTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRadiusDisconnectUnknownTypes.setStatus(_A)
_JuniRadiusDisconnectPacketsDropped_Type=Counter32
_JuniRadiusDisconnectPacketsDropped_Object=MibTableColumn
juniRadiusDisconnectPacketsDropped=_JuniRadiusDisconnectPacketsDropped_Object((1,3,6,1,4,1,4874,2,2,67,1,1,2,1,10),_JuniRadiusDisconnectPacketsDropped_Type())
juniRadiusDisconnectPacketsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRadiusDisconnectPacketsDropped.setStatus(_A)
_JuniRadiusDisconnectCfgClientTable_Object=MibTable
juniRadiusDisconnectCfgClientTable=_JuniRadiusDisconnectCfgClientTable_Object((1,3,6,1,4,1,4874,2,2,67,1,1,3))
if mibBuilder.loadTexts:juniRadiusDisconnectCfgClientTable.setStatus(_A)
_JuniRadiusDisconnectCfgClientEntry_Object=MibTableRow
juniRadiusDisconnectCfgClientEntry=_JuniRadiusDisconnectCfgClientEntry_Object((1,3,6,1,4,1,4874,2,2,67,1,1,3,1))
juniRadiusDisconnectCfgClientEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:juniRadiusDisconnectCfgClientEntry.setStatus(_A)
_JuniRadiusDisconnectCfgClientAddress_Type=IpAddress
_JuniRadiusDisconnectCfgClientAddress_Object=MibTableColumn
juniRadiusDisconnectCfgClientAddress=_JuniRadiusDisconnectCfgClientAddress_Object((1,3,6,1,4,1,4874,2,2,67,1,1,3,1,1),_JuniRadiusDisconnectCfgClientAddress_Type())
juniRadiusDisconnectCfgClientAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:juniRadiusDisconnectCfgClientAddress.setStatus(_A)
class _JuniRadiusDisconnectCfgClientPortNumber_Type(Integer32):defaultValue=1700;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_JuniRadiusDisconnectCfgClientPortNumber_Type.__name__=_E
_JuniRadiusDisconnectCfgClientPortNumber_Object=MibTableColumn
juniRadiusDisconnectCfgClientPortNumber=_JuniRadiusDisconnectCfgClientPortNumber_Object((1,3,6,1,4,1,4874,2,2,67,1,1,3,1,2),_JuniRadiusDisconnectCfgClientPortNumber_Type())
juniRadiusDisconnectCfgClientPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:juniRadiusDisconnectCfgClientPortNumber.setStatus(_A)
class _JuniRadiusDisconnectCfgKey_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_JuniRadiusDisconnectCfgKey_Type.__name__=_F
_JuniRadiusDisconnectCfgKey_Object=MibTableColumn
juniRadiusDisconnectCfgKey=_JuniRadiusDisconnectCfgKey_Object((1,3,6,1,4,1,4874,2,2,67,1,1,3,1,3),_JuniRadiusDisconnectCfgKey_Type())
juniRadiusDisconnectCfgKey.setMaxAccess(_D)
if mibBuilder.loadTexts:juniRadiusDisconnectCfgKey.setStatus(_A)
_JuniRadiusDisconnectCfgRowStatus_Type=RowStatus
_JuniRadiusDisconnectCfgRowStatus_Object=MibTableColumn
juniRadiusDisconnectCfgRowStatus=_JuniRadiusDisconnectCfgRowStatus_Object((1,3,6,1,4,1,4874,2,2,67,1,1,3,1,4),_JuniRadiusDisconnectCfgRowStatus_Type())
juniRadiusDisconnectCfgRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniRadiusDisconnectCfgRowStatus.setStatus(_A)
_JuniRadiusDisconnectMIBConformance_ObjectIdentity=ObjectIdentity
juniRadiusDisconnectMIBConformance=_JuniRadiusDisconnectMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,67,2))
_JuniRadiusDisconnectMIBCompliances_ObjectIdentity=ObjectIdentity
juniRadiusDisconnectMIBCompliances=_JuniRadiusDisconnectMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,67,2,1))
_JuniRadiusDisconnectMIBGroups_ObjectIdentity=ObjectIdentity
juniRadiusDisconnectMIBGroups=_JuniRadiusDisconnectMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,67,2,2))
juniRadiusDisconnectGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,67,2,2,1))
juniRadiusDisconnectGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:juniRadiusDisconnectGroup.setStatus(_A)
juniRadiusAuthDisconnectCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,67,2,1,1))
juniRadiusAuthDisconnectCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:juniRadiusAuthDisconnectCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'juniRadiusDisconnectMIB':juniRadiusDisconnectMIB,'juniRadiusDisconnectObjects':juniRadiusDisconnectObjects,'juniRadiusDisconnect':juniRadiusDisconnect,_J:juniRadiusDisconnectInvalidClientAddresses,'juniRadiusDisconnectClientTable':juniRadiusDisconnectClientTable,'juniRadiusDisconnectClientEntry':juniRadiusDisconnectClientEntry,_G:juniRadiusDisconnectClientAddress,_K:juniRadiusDisconnectClientPortNumber,_L:juniRadiusDisconnectRequests,_M:juniRadiusDisconnectAccepts,_N:juniRadiusDisconnectRejects,_O:juniRadiusDisconnectNoSecret,_P:juniRadiusDisconnectNoSessionIds,_Q:juniRadiusDisconnectBadAuthenticators,_R:juniRadiusDisconnectUnknownTypes,_S:juniRadiusDisconnectPacketsDropped,'juniRadiusDisconnectCfgClientTable':juniRadiusDisconnectCfgClientTable,'juniRadiusDisconnectCfgClientEntry':juniRadiusDisconnectCfgClientEntry,_I:juniRadiusDisconnectCfgClientAddress,_T:juniRadiusDisconnectCfgClientPortNumber,_U:juniRadiusDisconnectCfgKey,_V:juniRadiusDisconnectCfgRowStatus,'juniRadiusDisconnectMIBConformance':juniRadiusDisconnectMIBConformance,'juniRadiusDisconnectMIBCompliances':juniRadiusDisconnectMIBCompliances,'juniRadiusAuthDisconnectCompliance':juniRadiusAuthDisconnectCompliance,'juniRadiusDisconnectMIBGroups':juniRadiusDisconnectMIBGroups,_W:juniRadiusDisconnectGroup})