_f='juniDhcpv6LocalServerGroup'
_e='juniDhcpv6LocalServerAttributesMode'
_d='juniDhcpv6LocalServerBindingsIf'
_c='juniDhcpv6LocalServerBindingsExpireTime'
_b='juniDhcpv6LocalServerBindingsInfinite'
_a='juniDhcpv6LocalServerBindingsClientDuid'
_Z='juniDhcpv6LocalServerPacketsOut'
_Y='juniDhcpv6LocalServerPacketsIn'
_X='juniDhcpv6LocalServerBadMessages'
_W='juniDhcpv6LocalServerUnknownMessages'
_V='juniDhcpv6LocalServerTxFailedReplies'
_U='juniDhcpv6LocalServerTxSuccessfulReplies'
_T='juniDhcpv6LocalServerTxAdvertises'
_S='juniDhcpv6LocalServerTxReconfigures'
_R='juniDhcpv6LocalServerRxRebinds'
_Q='juniDhcpv6LocalServerRxConfirms'
_P='juniDhcpv6LocalServerRxInforms'
_O='juniDhcpv6LocalServerRxReleases'
_N='juniDhcpv6LocalServerRxDeclines'
_M='juniDhcpv6LocalServerRxRenews'
_L='juniDhcpv6LocalServerRxAccepts'
_K='juniDhcpv6LocalServerRxSolicits'
_J='juniDhcpv6LocalServerNumBindings'
_I='juniDhcpv6LocalServerMemUsage'
_H='not-accessible'
_G='juniDhcpv6LocalServerBindingsLength'
_F='juniDhcpv6LocalServerBindingsPrefix'
_E='Integer32'
_D='OctetString'
_C='read-only'
_B='Juniper-DHCPv6-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6AddressPrefix,=mibBuilder.importSymbols('IPV6-TC','Ipv6AddressPrefix')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeInterval','TruthValue')
juniDhcpv6MIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,69))
if mibBuilder.loadTexts:juniDhcpv6MIB.setRevisions(('2003-05-08 17:15',))
class JuniDhcpv6LocalServerModeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('localServerModeTypeEqualAccess',1),('localServerModeTypeStandalone',2)))
_JuniDhcpv6Objects_ObjectIdentity=ObjectIdentity
juniDhcpv6Objects=_JuniDhcpv6Objects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,69,1))
_JuniDhcpv6LocalServerObjects_ObjectIdentity=ObjectIdentity
juniDhcpv6LocalServerObjects=_JuniDhcpv6LocalServerObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,69,1,1))
_JuniDhcpv6LocalServerStatistics_ObjectIdentity=ObjectIdentity
juniDhcpv6LocalServerStatistics=_JuniDhcpv6LocalServerStatistics_ObjectIdentity((1,3,6,1,4,1,4874,2,2,69,1,1,1))
_JuniDhcpv6LocalServerMemUsage_Type=Counter32
_JuniDhcpv6LocalServerMemUsage_Object=MibScalar
juniDhcpv6LocalServerMemUsage=_JuniDhcpv6LocalServerMemUsage_Object((1,3,6,1,4,1,4874,2,2,69,1,1,1,1),_JuniDhcpv6LocalServerMemUsage_Type())
juniDhcpv6LocalServerMemUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerMemUsage.setStatus(_A)
_JuniDhcpv6LocalServerNumBindings_Type=Counter32
_JuniDhcpv6LocalServerNumBindings_Object=MibScalar
juniDhcpv6LocalServerNumBindings=_JuniDhcpv6LocalServerNumBindings_Object((1,3,6,1,4,1,4874,2,2,69,1,1,1,2),_JuniDhcpv6LocalServerNumBindings_Type())
juniDhcpv6LocalServerNumBindings.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerNumBindings.setStatus(_A)
_JuniDhcpv6LocalServerRxSolicits_Type=Counter32
_JuniDhcpv6LocalServerRxSolicits_Object=MibScalar
juniDhcpv6LocalServerRxSolicits=_JuniDhcpv6LocalServerRxSolicits_Object((1,3,6,1,4,1,4874,2,2,69,1,1,1,3),_JuniDhcpv6LocalServerRxSolicits_Type())
juniDhcpv6LocalServerRxSolicits.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerRxSolicits.setStatus(_A)
_JuniDhcpv6LocalServerRxAccepts_Type=Counter32
_JuniDhcpv6LocalServerRxAccepts_Object=MibScalar
juniDhcpv6LocalServerRxAccepts=_JuniDhcpv6LocalServerRxAccepts_Object((1,3,6,1,4,1,4874,2,2,69,1,1,1,4),_JuniDhcpv6LocalServerRxAccepts_Type())
juniDhcpv6LocalServerRxAccepts.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerRxAccepts.setStatus(_A)
_JuniDhcpv6LocalServerRxRenews_Type=Counter32
_JuniDhcpv6LocalServerRxRenews_Object=MibScalar
juniDhcpv6LocalServerRxRenews=_JuniDhcpv6LocalServerRxRenews_Object((1,3,6,1,4,1,4874,2,2,69,1,1,1,5),_JuniDhcpv6LocalServerRxRenews_Type())
juniDhcpv6LocalServerRxRenews.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerRxRenews.setStatus(_A)
_JuniDhcpv6LocalServerRxDeclines_Type=Counter32
_JuniDhcpv6LocalServerRxDeclines_Object=MibScalar
juniDhcpv6LocalServerRxDeclines=_JuniDhcpv6LocalServerRxDeclines_Object((1,3,6,1,4,1,4874,2,2,69,1,1,1,6),_JuniDhcpv6LocalServerRxDeclines_Type())
juniDhcpv6LocalServerRxDeclines.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerRxDeclines.setStatus(_A)
_JuniDhcpv6LocalServerRxReleases_Type=Counter32
_JuniDhcpv6LocalServerRxReleases_Object=MibScalar
juniDhcpv6LocalServerRxReleases=_JuniDhcpv6LocalServerRxReleases_Object((1,3,6,1,4,1,4874,2,2,69,1,1,1,7),_JuniDhcpv6LocalServerRxReleases_Type())
juniDhcpv6LocalServerRxReleases.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerRxReleases.setStatus(_A)
_JuniDhcpv6LocalServerRxInforms_Type=Counter32
_JuniDhcpv6LocalServerRxInforms_Object=MibScalar
juniDhcpv6LocalServerRxInforms=_JuniDhcpv6LocalServerRxInforms_Object((1,3,6,1,4,1,4874,2,2,69,1,1,1,8),_JuniDhcpv6LocalServerRxInforms_Type())
juniDhcpv6LocalServerRxInforms.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerRxInforms.setStatus(_A)
_JuniDhcpv6LocalServerRxConfirms_Type=Counter32
_JuniDhcpv6LocalServerRxConfirms_Object=MibScalar
juniDhcpv6LocalServerRxConfirms=_JuniDhcpv6LocalServerRxConfirms_Object((1,3,6,1,4,1,4874,2,2,69,1,1,1,9),_JuniDhcpv6LocalServerRxConfirms_Type())
juniDhcpv6LocalServerRxConfirms.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerRxConfirms.setStatus(_A)
_JuniDhcpv6LocalServerRxRebinds_Type=Counter32
_JuniDhcpv6LocalServerRxRebinds_Object=MibScalar
juniDhcpv6LocalServerRxRebinds=_JuniDhcpv6LocalServerRxRebinds_Object((1,3,6,1,4,1,4874,2,2,69,1,1,1,10),_JuniDhcpv6LocalServerRxRebinds_Type())
juniDhcpv6LocalServerRxRebinds.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerRxRebinds.setStatus(_A)
_JuniDhcpv6LocalServerTxReconfigures_Type=Counter32
_JuniDhcpv6LocalServerTxReconfigures_Object=MibScalar
juniDhcpv6LocalServerTxReconfigures=_JuniDhcpv6LocalServerTxReconfigures_Object((1,3,6,1,4,1,4874,2,2,69,1,1,1,11),_JuniDhcpv6LocalServerTxReconfigures_Type())
juniDhcpv6LocalServerTxReconfigures.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerTxReconfigures.setStatus(_A)
_JuniDhcpv6LocalServerTxAdvertises_Type=Counter32
_JuniDhcpv6LocalServerTxAdvertises_Object=MibScalar
juniDhcpv6LocalServerTxAdvertises=_JuniDhcpv6LocalServerTxAdvertises_Object((1,3,6,1,4,1,4874,2,2,69,1,1,1,12),_JuniDhcpv6LocalServerTxAdvertises_Type())
juniDhcpv6LocalServerTxAdvertises.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerTxAdvertises.setStatus(_A)
_JuniDhcpv6LocalServerTxSuccessfulReplies_Type=Counter32
_JuniDhcpv6LocalServerTxSuccessfulReplies_Object=MibScalar
juniDhcpv6LocalServerTxSuccessfulReplies=_JuniDhcpv6LocalServerTxSuccessfulReplies_Object((1,3,6,1,4,1,4874,2,2,69,1,1,1,13),_JuniDhcpv6LocalServerTxSuccessfulReplies_Type())
juniDhcpv6LocalServerTxSuccessfulReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerTxSuccessfulReplies.setStatus(_A)
_JuniDhcpv6LocalServerTxFailedReplies_Type=Counter32
_JuniDhcpv6LocalServerTxFailedReplies_Object=MibScalar
juniDhcpv6LocalServerTxFailedReplies=_JuniDhcpv6LocalServerTxFailedReplies_Object((1,3,6,1,4,1,4874,2,2,69,1,1,1,14),_JuniDhcpv6LocalServerTxFailedReplies_Type())
juniDhcpv6LocalServerTxFailedReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerTxFailedReplies.setStatus(_A)
_JuniDhcpv6LocalServerUnknownMessages_Type=Counter32
_JuniDhcpv6LocalServerUnknownMessages_Object=MibScalar
juniDhcpv6LocalServerUnknownMessages=_JuniDhcpv6LocalServerUnknownMessages_Object((1,3,6,1,4,1,4874,2,2,69,1,1,1,15),_JuniDhcpv6LocalServerUnknownMessages_Type())
juniDhcpv6LocalServerUnknownMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerUnknownMessages.setStatus(_A)
_JuniDhcpv6LocalServerBadMessages_Type=Counter32
_JuniDhcpv6LocalServerBadMessages_Object=MibScalar
juniDhcpv6LocalServerBadMessages=_JuniDhcpv6LocalServerBadMessages_Object((1,3,6,1,4,1,4874,2,2,69,1,1,1,16),_JuniDhcpv6LocalServerBadMessages_Type())
juniDhcpv6LocalServerBadMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerBadMessages.setStatus(_A)
_JuniDhcpv6LocalServerPacketsIn_Type=Counter32
_JuniDhcpv6LocalServerPacketsIn_Object=MibScalar
juniDhcpv6LocalServerPacketsIn=_JuniDhcpv6LocalServerPacketsIn_Object((1,3,6,1,4,1,4874,2,2,69,1,1,1,17),_JuniDhcpv6LocalServerPacketsIn_Type())
juniDhcpv6LocalServerPacketsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerPacketsIn.setStatus(_A)
_JuniDhcpv6LocalServerPacketsOut_Type=Counter32
_JuniDhcpv6LocalServerPacketsOut_Object=MibScalar
juniDhcpv6LocalServerPacketsOut=_JuniDhcpv6LocalServerPacketsOut_Object((1,3,6,1,4,1,4874,2,2,69,1,1,1,18),_JuniDhcpv6LocalServerPacketsOut_Type())
juniDhcpv6LocalServerPacketsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerPacketsOut.setStatus(_A)
_JuniDhcpv6LocalServerAttributes_ObjectIdentity=ObjectIdentity
juniDhcpv6LocalServerAttributes=_JuniDhcpv6LocalServerAttributes_ObjectIdentity((1,3,6,1,4,1,4874,2,2,69,1,1,2))
_JuniDhcpv6LocalServerAttributesMode_Type=JuniDhcpv6LocalServerModeType
_JuniDhcpv6LocalServerAttributesMode_Object=MibScalar
juniDhcpv6LocalServerAttributesMode=_JuniDhcpv6LocalServerAttributesMode_Object((1,3,6,1,4,1,4874,2,2,69,1,1,2,1),_JuniDhcpv6LocalServerAttributesMode_Type())
juniDhcpv6LocalServerAttributesMode.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerAttributesMode.setStatus(_A)
_JuniDhcpv6LocalServerBindings_ObjectIdentity=ObjectIdentity
juniDhcpv6LocalServerBindings=_JuniDhcpv6LocalServerBindings_ObjectIdentity((1,3,6,1,4,1,4874,2,2,69,1,1,3))
_JuniDhcpv6LocalServerBindingsTable_Object=MibTable
juniDhcpv6LocalServerBindingsTable=_JuniDhcpv6LocalServerBindingsTable_Object((1,3,6,1,4,1,4874,2,2,69,1,1,3,1))
if mibBuilder.loadTexts:juniDhcpv6LocalServerBindingsTable.setStatus(_A)
_JuniDhcpv6LocalServerBindingsEntry_Object=MibTableRow
juniDhcpv6LocalServerBindingsEntry=_JuniDhcpv6LocalServerBindingsEntry_Object((1,3,6,1,4,1,4874,2,2,69,1,1,3,1,1))
juniDhcpv6LocalServerBindingsEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:juniDhcpv6LocalServerBindingsEntry.setStatus(_A)
_JuniDhcpv6LocalServerBindingsPrefix_Type=Ipv6AddressPrefix
_JuniDhcpv6LocalServerBindingsPrefix_Object=MibTableColumn
juniDhcpv6LocalServerBindingsPrefix=_JuniDhcpv6LocalServerBindingsPrefix_Object((1,3,6,1,4,1,4874,2,2,69,1,1,3,1,1,1),_JuniDhcpv6LocalServerBindingsPrefix_Type())
juniDhcpv6LocalServerBindingsPrefix.setMaxAccess(_H)
if mibBuilder.loadTexts:juniDhcpv6LocalServerBindingsPrefix.setStatus(_A)
class _JuniDhcpv6LocalServerBindingsLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_JuniDhcpv6LocalServerBindingsLength_Type.__name__=_E
_JuniDhcpv6LocalServerBindingsLength_Object=MibTableColumn
juniDhcpv6LocalServerBindingsLength=_JuniDhcpv6LocalServerBindingsLength_Object((1,3,6,1,4,1,4874,2,2,69,1,1,3,1,1,2),_JuniDhcpv6LocalServerBindingsLength_Type())
juniDhcpv6LocalServerBindingsLength.setMaxAccess(_H)
if mibBuilder.loadTexts:juniDhcpv6LocalServerBindingsLength.setStatus(_A)
class _JuniDhcpv6LocalServerBindingsClientDuid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,130))
_JuniDhcpv6LocalServerBindingsClientDuid_Type.__name__=_D
_JuniDhcpv6LocalServerBindingsClientDuid_Object=MibTableColumn
juniDhcpv6LocalServerBindingsClientDuid=_JuniDhcpv6LocalServerBindingsClientDuid_Object((1,3,6,1,4,1,4874,2,2,69,1,1,3,1,1,3),_JuniDhcpv6LocalServerBindingsClientDuid_Type())
juniDhcpv6LocalServerBindingsClientDuid.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerBindingsClientDuid.setStatus(_A)
_JuniDhcpv6LocalServerBindingsInfinite_Type=TruthValue
_JuniDhcpv6LocalServerBindingsInfinite_Object=MibTableColumn
juniDhcpv6LocalServerBindingsInfinite=_JuniDhcpv6LocalServerBindingsInfinite_Object((1,3,6,1,4,1,4874,2,2,69,1,1,3,1,1,4),_JuniDhcpv6LocalServerBindingsInfinite_Type())
juniDhcpv6LocalServerBindingsInfinite.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerBindingsInfinite.setStatus(_A)
_JuniDhcpv6LocalServerBindingsExpireTime_Type=TimeInterval
_JuniDhcpv6LocalServerBindingsExpireTime_Object=MibTableColumn
juniDhcpv6LocalServerBindingsExpireTime=_JuniDhcpv6LocalServerBindingsExpireTime_Object((1,3,6,1,4,1,4874,2,2,69,1,1,3,1,1,5),_JuniDhcpv6LocalServerBindingsExpireTime_Type())
juniDhcpv6LocalServerBindingsExpireTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerBindingsExpireTime.setStatus(_A)
class _JuniDhcpv6LocalServerBindingsIf_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_JuniDhcpv6LocalServerBindingsIf_Type.__name__=_D
_JuniDhcpv6LocalServerBindingsIf_Object=MibTableColumn
juniDhcpv6LocalServerBindingsIf=_JuniDhcpv6LocalServerBindingsIf_Object((1,3,6,1,4,1,4874,2,2,69,1,1,3,1,1,6),_JuniDhcpv6LocalServerBindingsIf_Type())
juniDhcpv6LocalServerBindingsIf.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDhcpv6LocalServerBindingsIf.setStatus(_A)
_JuniDhcpv6MIBConformance_ObjectIdentity=ObjectIdentity
juniDhcpv6MIBConformance=_JuniDhcpv6MIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,69,2))
_JuniDhcpv6MIBCompliances_ObjectIdentity=ObjectIdentity
juniDhcpv6MIBCompliances=_JuniDhcpv6MIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,69,2,1))
_JuniDhcpv6MIBGroups_ObjectIdentity=ObjectIdentity
juniDhcpv6MIBGroups=_JuniDhcpv6MIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,69,2,2))
juniDhcpv6LocalServerGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,69,2,2,1))
juniDhcpv6LocalServerGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:juniDhcpv6LocalServerGroup.setStatus(_A)
juniDhcpv6Compliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,69,2,1,1))
juniDhcpv6Compliance2.setObjects((_B,_f))
if mibBuilder.loadTexts:juniDhcpv6Compliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'JuniDhcpv6LocalServerModeType':JuniDhcpv6LocalServerModeType,'juniDhcpv6MIB':juniDhcpv6MIB,'juniDhcpv6Objects':juniDhcpv6Objects,'juniDhcpv6LocalServerObjects':juniDhcpv6LocalServerObjects,'juniDhcpv6LocalServerStatistics':juniDhcpv6LocalServerStatistics,_I:juniDhcpv6LocalServerMemUsage,_J:juniDhcpv6LocalServerNumBindings,_K:juniDhcpv6LocalServerRxSolicits,_L:juniDhcpv6LocalServerRxAccepts,_M:juniDhcpv6LocalServerRxRenews,_N:juniDhcpv6LocalServerRxDeclines,_O:juniDhcpv6LocalServerRxReleases,_P:juniDhcpv6LocalServerRxInforms,_Q:juniDhcpv6LocalServerRxConfirms,_R:juniDhcpv6LocalServerRxRebinds,_S:juniDhcpv6LocalServerTxReconfigures,_T:juniDhcpv6LocalServerTxAdvertises,_U:juniDhcpv6LocalServerTxSuccessfulReplies,_V:juniDhcpv6LocalServerTxFailedReplies,_W:juniDhcpv6LocalServerUnknownMessages,_X:juniDhcpv6LocalServerBadMessages,_Y:juniDhcpv6LocalServerPacketsIn,_Z:juniDhcpv6LocalServerPacketsOut,'juniDhcpv6LocalServerAttributes':juniDhcpv6LocalServerAttributes,_e:juniDhcpv6LocalServerAttributesMode,'juniDhcpv6LocalServerBindings':juniDhcpv6LocalServerBindings,'juniDhcpv6LocalServerBindingsTable':juniDhcpv6LocalServerBindingsTable,'juniDhcpv6LocalServerBindingsEntry':juniDhcpv6LocalServerBindingsEntry,_F:juniDhcpv6LocalServerBindingsPrefix,_G:juniDhcpv6LocalServerBindingsLength,_a:juniDhcpv6LocalServerBindingsClientDuid,_b:juniDhcpv6LocalServerBindingsInfinite,_c:juniDhcpv6LocalServerBindingsExpireTime,_d:juniDhcpv6LocalServerBindingsIf,'juniDhcpv6MIBConformance':juniDhcpv6MIBConformance,'juniDhcpv6MIBCompliances':juniDhcpv6MIBCompliances,'juniDhcpv6Compliance2':juniDhcpv6Compliance2,'juniDhcpv6MIBGroups':juniDhcpv6MIBGroups,_f:juniDhcpv6LocalServerGroup})