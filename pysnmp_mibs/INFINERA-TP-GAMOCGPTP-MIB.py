_N='gamOcgPtpGroup'
_M='gamOcgPtpInlineDcmType'
_L='gamOcgPtpPmHistStatsEnable'
_K='gamOcgPtpDiscoveredRemoteTP'
_J='gamOcgPtpProvisionedOcgTP'
_I='gamOcgPtpDiscoveredOcgTP'
_H='read-only'
_G='Integer32'
_F='InfnDcmType'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='INFINERA-TP-GAMOCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnDcmType,=mibBuilder.importSymbols('INFINERA-TC-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gamOcgPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,8))
if mibBuilder.loadTexts:gamOcgPtpMIB.setRevisions(('2008-10-20 00:00',))
_GamOcgPtpTable_Object=MibTable
gamOcgPtpTable=_GamOcgPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,8,1))
if mibBuilder.loadTexts:gamOcgPtpTable.setStatus(_A)
_GamOcgPtpEntry_Object=MibTableRow
gamOcgPtpEntry=_GamOcgPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,8,1,1))
gamOcgPtpEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:gamOcgPtpEntry.setStatus(_A)
_GamOcgPtpDiscoveredOcgTP_Type=DisplayString
_GamOcgPtpDiscoveredOcgTP_Object=MibTableColumn
gamOcgPtpDiscoveredOcgTP=_GamOcgPtpDiscoveredOcgTP_Object((1,3,6,1,4,1,21296,2,2,2,2,8,1,1,1),_GamOcgPtpDiscoveredOcgTP_Type())
gamOcgPtpDiscoveredOcgTP.setMaxAccess(_H)
if mibBuilder.loadTexts:gamOcgPtpDiscoveredOcgTP.setStatus(_A)
_GamOcgPtpProvisionedOcgTP_Type=DisplayString
_GamOcgPtpProvisionedOcgTP_Object=MibTableColumn
gamOcgPtpProvisionedOcgTP=_GamOcgPtpProvisionedOcgTP_Object((1,3,6,1,4,1,21296,2,2,2,2,8,1,1,2),_GamOcgPtpProvisionedOcgTP_Type())
gamOcgPtpProvisionedOcgTP.setMaxAccess(_C)
if mibBuilder.loadTexts:gamOcgPtpProvisionedOcgTP.setStatus(_A)
_GamOcgPtpDiscoveredRemoteTP_Type=DisplayString
_GamOcgPtpDiscoveredRemoteTP_Object=MibTableColumn
gamOcgPtpDiscoveredRemoteTP=_GamOcgPtpDiscoveredRemoteTP_Object((1,3,6,1,4,1,21296,2,2,2,2,8,1,1,3),_GamOcgPtpDiscoveredRemoteTP_Type())
gamOcgPtpDiscoveredRemoteTP.setMaxAccess(_H)
if mibBuilder.loadTexts:gamOcgPtpDiscoveredRemoteTP.setStatus(_A)
class _GamOcgPtpPmHistStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_GamOcgPtpPmHistStatsEnable_Type.__name__=_G
_GamOcgPtpPmHistStatsEnable_Object=MibTableColumn
gamOcgPtpPmHistStatsEnable=_GamOcgPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,8,1,1,4),_GamOcgPtpPmHistStatsEnable_Type())
gamOcgPtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:gamOcgPtpPmHistStatsEnable.setStatus(_A)
class _GamOcgPtpInlineDcmType_Type(InfnDcmType):defaultValue=25
_GamOcgPtpInlineDcmType_Type.__name__=_F
_GamOcgPtpInlineDcmType_Object=MibTableColumn
gamOcgPtpInlineDcmType=_GamOcgPtpInlineDcmType_Object((1,3,6,1,4,1,21296,2,2,2,2,8,1,1,5),_GamOcgPtpInlineDcmType_Type())
gamOcgPtpInlineDcmType.setMaxAccess(_C)
if mibBuilder.loadTexts:gamOcgPtpInlineDcmType.setStatus('obsolete')
_GamOcgPtpConformance_ObjectIdentity=ObjectIdentity
gamOcgPtpConformance=_GamOcgPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,8,3))
_GamOcgPtpCompliances_ObjectIdentity=ObjectIdentity
gamOcgPtpCompliances=_GamOcgPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,8,3,1))
_GamOcgPtpGroups_ObjectIdentity=ObjectIdentity
gamOcgPtpGroups=_GamOcgPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,8,3,2))
gamOcgPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,8,3,2,1))
gamOcgPtpGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:gamOcgPtpGroup.setStatus(_A)
gamOcgPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,8,3,1,1))
gamOcgPtpCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:gamOcgPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'gamOcgPtpMIB':gamOcgPtpMIB,'gamOcgPtpTable':gamOcgPtpTable,'gamOcgPtpEntry':gamOcgPtpEntry,_I:gamOcgPtpDiscoveredOcgTP,_J:gamOcgPtpProvisionedOcgTP,_K:gamOcgPtpDiscoveredRemoteTP,_L:gamOcgPtpPmHistStatsEnable,_M:gamOcgPtpInlineDcmType,'gamOcgPtpConformance':gamOcgPtpConformance,'gamOcgPtpCompliances':gamOcgPtpCompliances,'gamOcgPtpCompliance':gamOcgPtpCompliance,'gamOcgPtpGroups':gamOcgPtpGroups,_N:gamOcgPtpGroup})