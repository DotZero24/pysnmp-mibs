_b='juniHttpInterfaceGroup'
_a='juniHttpDaemonStatsGroup'
_Z='juniHttpInterfaceRedirectUrl'
_Y='juniHttpInterfaceRowStatus'
_X='juniHttpDaemonStatsUnknownUrl'
_W='juniHttpDaemonStatsHtmlError'
_V='juniHttpDaemonStatsServed'
_U='juniHttpDaemonStatsAged'
_T='juniHttpDaemonStatsRemove'
_S='juniHttpDaemonStatsCreate'
_R='juniHttpDaemonStatsNoResource'
_Q='juniHttpDaemonStatsAccDeny'
_P='juniHttpDaemonStatsSameHost'
_O='juniHttpDaemonStatsDisabled'
_N='juniHttpDaemonStatsEnabled'
_M='juniHttpDaemonSameAddressLimit'
_L='juniHttpDaemonPort'
_K='juniHttpDaemonAccessListName'
_J='juniHttpDaemonRowStatus'
_I='juniHttpInterfaceIndex'
_H='read-create'
_G='Unsigned32'
_F='Integer32'
_E='DisplayString'
_D='read-write'
_C='read-only'
_B='Juniper-HTTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
juniHttpMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,78))
if mibBuilder.loadTexts:juniHttpMIB.setRevisions(('2005-08-22 15:51',))
_JuniHttpObjects_ObjectIdentity=ObjectIdentity
juniHttpObjects=_JuniHttpObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,78,1))
_JuniHttpDaemon_ObjectIdentity=ObjectIdentity
juniHttpDaemon=_JuniHttpDaemon_ObjectIdentity((1,3,6,1,4,1,4874,2,2,78,1,1))
_JuniHttpDaemonRowStatus_Type=RowStatus
_JuniHttpDaemonRowStatus_Object=MibScalar
juniHttpDaemonRowStatus=_JuniHttpDaemonRowStatus_Object((1,3,6,1,4,1,4874,2,2,78,1,1,1),_JuniHttpDaemonRowStatus_Type())
juniHttpDaemonRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:juniHttpDaemonRowStatus.setStatus(_A)
class _JuniHttpDaemonAccessListName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_JuniHttpDaemonAccessListName_Type.__name__=_E
_JuniHttpDaemonAccessListName_Object=MibScalar
juniHttpDaemonAccessListName=_JuniHttpDaemonAccessListName_Object((1,3,6,1,4,1,4874,2,2,78,1,1,2),_JuniHttpDaemonAccessListName_Type())
juniHttpDaemonAccessListName.setMaxAccess(_D)
if mibBuilder.loadTexts:juniHttpDaemonAccessListName.setStatus(_A)
class _JuniHttpDaemonPort_Type(Integer32):defaultValue=80
_JuniHttpDaemonPort_Type.__name__=_F
_JuniHttpDaemonPort_Object=MibScalar
juniHttpDaemonPort=_JuniHttpDaemonPort_Object((1,3,6,1,4,1,4874,2,2,78,1,1,3),_JuniHttpDaemonPort_Type())
juniHttpDaemonPort.setMaxAccess(_D)
if mibBuilder.loadTexts:juniHttpDaemonPort.setStatus(_A)
class _JuniHttpDaemonSameAddressLimit_Type(Unsigned32):defaultValue=10
_JuniHttpDaemonSameAddressLimit_Type.__name__=_G
_JuniHttpDaemonSameAddressLimit_Object=MibScalar
juniHttpDaemonSameAddressLimit=_JuniHttpDaemonSameAddressLimit_Object((1,3,6,1,4,1,4874,2,2,78,1,1,4),_JuniHttpDaemonSameAddressLimit_Type())
juniHttpDaemonSameAddressLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:juniHttpDaemonSameAddressLimit.setStatus(_A)
_JuniHttpDaemonStats_ObjectIdentity=ObjectIdentity
juniHttpDaemonStats=_JuniHttpDaemonStats_ObjectIdentity((1,3,6,1,4,1,4874,2,2,78,1,2))
_JuniHttpDaemonStatsEnabled_Type=Counter32
_JuniHttpDaemonStatsEnabled_Object=MibScalar
juniHttpDaemonStatsEnabled=_JuniHttpDaemonStatsEnabled_Object((1,3,6,1,4,1,4874,2,2,78,1,2,1),_JuniHttpDaemonStatsEnabled_Type())
juniHttpDaemonStatsEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHttpDaemonStatsEnabled.setStatus(_A)
_JuniHttpDaemonStatsDisabled_Type=Counter32
_JuniHttpDaemonStatsDisabled_Object=MibScalar
juniHttpDaemonStatsDisabled=_JuniHttpDaemonStatsDisabled_Object((1,3,6,1,4,1,4874,2,2,78,1,2,2),_JuniHttpDaemonStatsDisabled_Type())
juniHttpDaemonStatsDisabled.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHttpDaemonStatsDisabled.setStatus(_A)
_JuniHttpDaemonStatsSameHost_Type=Counter32
_JuniHttpDaemonStatsSameHost_Object=MibScalar
juniHttpDaemonStatsSameHost=_JuniHttpDaemonStatsSameHost_Object((1,3,6,1,4,1,4874,2,2,78,1,2,3),_JuniHttpDaemonStatsSameHost_Type())
juniHttpDaemonStatsSameHost.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHttpDaemonStatsSameHost.setStatus(_A)
_JuniHttpDaemonStatsAccDeny_Type=Counter32
_JuniHttpDaemonStatsAccDeny_Object=MibScalar
juniHttpDaemonStatsAccDeny=_JuniHttpDaemonStatsAccDeny_Object((1,3,6,1,4,1,4874,2,2,78,1,2,4),_JuniHttpDaemonStatsAccDeny_Type())
juniHttpDaemonStatsAccDeny.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHttpDaemonStatsAccDeny.setStatus(_A)
_JuniHttpDaemonStatsNoResource_Type=Counter32
_JuniHttpDaemonStatsNoResource_Object=MibScalar
juniHttpDaemonStatsNoResource=_JuniHttpDaemonStatsNoResource_Object((1,3,6,1,4,1,4874,2,2,78,1,2,5),_JuniHttpDaemonStatsNoResource_Type())
juniHttpDaemonStatsNoResource.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHttpDaemonStatsNoResource.setStatus(_A)
_JuniHttpDaemonStatsCreate_Type=Counter32
_JuniHttpDaemonStatsCreate_Object=MibScalar
juniHttpDaemonStatsCreate=_JuniHttpDaemonStatsCreate_Object((1,3,6,1,4,1,4874,2,2,78,1,2,6),_JuniHttpDaemonStatsCreate_Type())
juniHttpDaemonStatsCreate.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHttpDaemonStatsCreate.setStatus(_A)
_JuniHttpDaemonStatsRemove_Type=Counter32
_JuniHttpDaemonStatsRemove_Object=MibScalar
juniHttpDaemonStatsRemove=_JuniHttpDaemonStatsRemove_Object((1,3,6,1,4,1,4874,2,2,78,1,2,7),_JuniHttpDaemonStatsRemove_Type())
juniHttpDaemonStatsRemove.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHttpDaemonStatsRemove.setStatus(_A)
_JuniHttpDaemonStatsAged_Type=Counter32
_JuniHttpDaemonStatsAged_Object=MibScalar
juniHttpDaemonStatsAged=_JuniHttpDaemonStatsAged_Object((1,3,6,1,4,1,4874,2,2,78,1,2,8),_JuniHttpDaemonStatsAged_Type())
juniHttpDaemonStatsAged.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHttpDaemonStatsAged.setStatus(_A)
_JuniHttpDaemonStatsServed_Type=Counter32
_JuniHttpDaemonStatsServed_Object=MibScalar
juniHttpDaemonStatsServed=_JuniHttpDaemonStatsServed_Object((1,3,6,1,4,1,4874,2,2,78,1,2,9),_JuniHttpDaemonStatsServed_Type())
juniHttpDaemonStatsServed.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHttpDaemonStatsServed.setStatus(_A)
_JuniHttpDaemonStatsHtmlError_Type=Counter32
_JuniHttpDaemonStatsHtmlError_Object=MibScalar
juniHttpDaemonStatsHtmlError=_JuniHttpDaemonStatsHtmlError_Object((1,3,6,1,4,1,4874,2,2,78,1,2,10),_JuniHttpDaemonStatsHtmlError_Type())
juniHttpDaemonStatsHtmlError.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHttpDaemonStatsHtmlError.setStatus(_A)
_JuniHttpDaemonStatsUnknownUrl_Type=Counter32
_JuniHttpDaemonStatsUnknownUrl_Object=MibScalar
juniHttpDaemonStatsUnknownUrl=_JuniHttpDaemonStatsUnknownUrl_Object((1,3,6,1,4,1,4874,2,2,78,1,2,11),_JuniHttpDaemonStatsUnknownUrl_Type())
juniHttpDaemonStatsUnknownUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHttpDaemonStatsUnknownUrl.setStatus(_A)
_JuniHttpInterfaces_ObjectIdentity=ObjectIdentity
juniHttpInterfaces=_JuniHttpInterfaces_ObjectIdentity((1,3,6,1,4,1,4874,2,2,78,1,3))
_JuniHttpInterfaceTable_Object=MibTable
juniHttpInterfaceTable=_JuniHttpInterfaceTable_Object((1,3,6,1,4,1,4874,2,2,78,1,3,1))
if mibBuilder.loadTexts:juniHttpInterfaceTable.setStatus(_A)
_JuniHttpInterfaceEntry_Object=MibTableRow
juniHttpInterfaceEntry=_JuniHttpInterfaceEntry_Object((1,3,6,1,4,1,4874,2,2,78,1,3,1,1))
juniHttpInterfaceEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:juniHttpInterfaceEntry.setStatus(_A)
_JuniHttpInterfaceIndex_Type=InterfaceIndex
_JuniHttpInterfaceIndex_Object=MibTableColumn
juniHttpInterfaceIndex=_JuniHttpInterfaceIndex_Object((1,3,6,1,4,1,4874,2,2,78,1,3,1,1,1),_JuniHttpInterfaceIndex_Type())
juniHttpInterfaceIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:juniHttpInterfaceIndex.setStatus(_A)
_JuniHttpInterfaceRowStatus_Type=RowStatus
_JuniHttpInterfaceRowStatus_Object=MibTableColumn
juniHttpInterfaceRowStatus=_JuniHttpInterfaceRowStatus_Object((1,3,6,1,4,1,4874,2,2,78,1,3,1,1,2),_JuniHttpInterfaceRowStatus_Type())
juniHttpInterfaceRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:juniHttpInterfaceRowStatus.setStatus(_A)
class _JuniHttpInterfaceRedirectUrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_JuniHttpInterfaceRedirectUrl_Type.__name__=_E
_JuniHttpInterfaceRedirectUrl_Object=MibTableColumn
juniHttpInterfaceRedirectUrl=_JuniHttpInterfaceRedirectUrl_Object((1,3,6,1,4,1,4874,2,2,78,1,3,1,1,3),_JuniHttpInterfaceRedirectUrl_Type())
juniHttpInterfaceRedirectUrl.setMaxAccess(_D)
if mibBuilder.loadTexts:juniHttpInterfaceRedirectUrl.setStatus(_A)
_JuniHttpConformance_ObjectIdentity=ObjectIdentity
juniHttpConformance=_JuniHttpConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,78,4))
_JuniHttpCompliances_ObjectIdentity=ObjectIdentity
juniHttpCompliances=_JuniHttpCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,78,4,1))
_JuniHttpGroups_ObjectIdentity=ObjectIdentity
juniHttpGroups=_JuniHttpGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,78,4,2))
juniHttpGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,78,4,2,1))
juniHttpGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:juniHttpGroup.setStatus(_A)
juniHttpDaemonStatsGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,78,4,2,2))
juniHttpDaemonStatsGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:juniHttpDaemonStatsGroup.setStatus(_A)
juniHttpInterfaceGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,78,4,2,3))
juniHttpInterfaceGroup.setObjects(*((_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:juniHttpInterfaceGroup.setStatus(_A)
juniHttpCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,78,4,1,1))
juniHttpCompliance.setObjects(*((_B,'juniHttpDaemonGroup'),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:juniHttpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'juniHttpMIB':juniHttpMIB,'juniHttpObjects':juniHttpObjects,'juniHttpDaemon':juniHttpDaemon,_J:juniHttpDaemonRowStatus,_K:juniHttpDaemonAccessListName,_L:juniHttpDaemonPort,_M:juniHttpDaemonSameAddressLimit,'juniHttpDaemonStats':juniHttpDaemonStats,_N:juniHttpDaemonStatsEnabled,_O:juniHttpDaemonStatsDisabled,_P:juniHttpDaemonStatsSameHost,_Q:juniHttpDaemonStatsAccDeny,_R:juniHttpDaemonStatsNoResource,_S:juniHttpDaemonStatsCreate,_T:juniHttpDaemonStatsRemove,_U:juniHttpDaemonStatsAged,_V:juniHttpDaemonStatsServed,_W:juniHttpDaemonStatsHtmlError,_X:juniHttpDaemonStatsUnknownUrl,'juniHttpInterfaces':juniHttpInterfaces,'juniHttpInterfaceTable':juniHttpInterfaceTable,'juniHttpInterfaceEntry':juniHttpInterfaceEntry,_I:juniHttpInterfaceIndex,_Y:juniHttpInterfaceRowStatus,_Z:juniHttpInterfaceRedirectUrl,'juniHttpConformance':juniHttpConformance,'juniHttpCompliances':juniHttpCompliances,'juniHttpCompliance':juniHttpCompliance,'juniHttpGroups':juniHttpGroups,'juniHttpGroup':juniHttpGroup,_a:juniHttpDaemonStatsGroup,_b:juniHttpInterfaceGroup})