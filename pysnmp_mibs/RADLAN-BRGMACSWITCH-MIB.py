_G='unsupported'
_F='supported'
_E='TruthValue'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
rlBrgMacSwitch=ModuleIdentity((1,3,6,1,4,1,89,50))
if mibBuilder.loadTexts:rlBrgMacSwitch.setRevisions(('2007-01-02 00:00',))
_RlBrgMacSwVersion_Type=Integer32
_RlBrgMacSwVersion_Object=MibScalar
rlBrgMacSwVersion=_RlBrgMacSwVersion_Object((1,3,6,1,4,1,89,50,1),_RlBrgMacSwVersion_Type())
rlBrgMacSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBrgMacSwVersion.setStatus(_A)
_RlBrgMacSwMaxTableNumber_Type=Integer32
_RlBrgMacSwMaxTableNumber_Object=MibScalar
rlBrgMacSwMaxTableNumber=_RlBrgMacSwMaxTableNumber_Object((1,3,6,1,4,1,89,50,2),_RlBrgMacSwMaxTableNumber_Type())
rlBrgMacSwMaxTableNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBrgMacSwMaxTableNumber.setStatus(_A)
class _RlBrgMacSwDynamicTables_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RlBrgMacSwDynamicTables_Type.__name__=_C
_RlBrgMacSwDynamicTables_Object=MibScalar
rlBrgMacSwDynamicTables=_RlBrgMacSwDynamicTables_Object((1,3,6,1,4,1,89,50,3),_RlBrgMacSwDynamicTables_Type())
rlBrgMacSwDynamicTables.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBrgMacSwDynamicTables.setStatus(_A)
class _RlBrgMacSwOldEntryDeleteMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('refreshFlag',1),('agingFlag',2),('agingTime',3),('boundaries',4)))
_RlBrgMacSwOldEntryDeleteMode_Type.__name__=_C
_RlBrgMacSwOldEntryDeleteMode_Object=MibScalar
rlBrgMacSwOldEntryDeleteMode=_RlBrgMacSwOldEntryDeleteMode_Object((1,3,6,1,4,1,89,50,5),_RlBrgMacSwOldEntryDeleteMode_Type())
rlBrgMacSwOldEntryDeleteMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBrgMacSwOldEntryDeleteMode.setStatus(_A)
class _RlBrgMacSwSpanningTree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RlBrgMacSwSpanningTree_Type.__name__=_C
_RlBrgMacSwSpanningTree_Object=MibScalar
rlBrgMacSwSpanningTree=_RlBrgMacSwSpanningTree_Object((1,3,6,1,4,1,89,50,6),_RlBrgMacSwSpanningTree_Type())
rlBrgMacSwSpanningTree.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBrgMacSwSpanningTree.setStatus(_A)
class _RlBrgMacSwKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('macOnly',1),('tagAndMac',2)))
_RlBrgMacSwKeyType_Type.__name__=_C
_RlBrgMacSwKeyType_Object=MibScalar
rlBrgMacSwKeyType=_RlBrgMacSwKeyType_Object((1,3,6,1,4,1,89,50,7),_RlBrgMacSwKeyType_Type())
rlBrgMacSwKeyType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBrgMacSwKeyType.setStatus(_A)
_RlBrgMacSwYellowBoundary_Type=Integer32
_RlBrgMacSwYellowBoundary_Object=MibScalar
rlBrgMacSwYellowBoundary=_RlBrgMacSwYellowBoundary_Object((1,3,6,1,4,1,89,50,8),_RlBrgMacSwYellowBoundary_Type())
rlBrgMacSwYellowBoundary.setMaxAccess(_D)
if mibBuilder.loadTexts:rlBrgMacSwYellowBoundary.setStatus(_A)
_RlBrgMacSwRedBoundary_Type=Integer32
_RlBrgMacSwRedBoundary_Object=MibScalar
rlBrgMacSwRedBoundary=_RlBrgMacSwRedBoundary_Object((1,3,6,1,4,1,89,50,9),_RlBrgMacSwRedBoundary_Type())
rlBrgMacSwRedBoundary.setMaxAccess(_D)
if mibBuilder.loadTexts:rlBrgMacSwRedBoundary.setStatus(_A)
class _RlBrgMacSwTrapEnable_Type(TruthValue):defaultValue=2
_RlBrgMacSwTrapEnable_Type.__name__=_E
_RlBrgMacSwTrapEnable_Object=MibScalar
rlBrgMacSwTrapEnable=_RlBrgMacSwTrapEnable_Object((1,3,6,1,4,1,89,50,10),_RlBrgMacSwTrapEnable_Type())
rlBrgMacSwTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rlBrgMacSwTrapEnable.setStatus(_A)
_RlBrgMacSwOperTrapCount_Type=Integer32
_RlBrgMacSwOperTrapCount_Object=MibScalar
rlBrgMacSwOperTrapCount=_RlBrgMacSwOperTrapCount_Object((1,3,6,1,4,1,89,50,11),_RlBrgMacSwOperTrapCount_Type())
rlBrgMacSwOperTrapCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBrgMacSwOperTrapCount.setStatus(_A)
class _RlBrgMacSwAdminTrapFrequency_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_RlBrgMacSwAdminTrapFrequency_Type.__name__=_C
_RlBrgMacSwAdminTrapFrequency_Object=MibScalar
rlBrgMacSwAdminTrapFrequency=_RlBrgMacSwAdminTrapFrequency_Object((1,3,6,1,4,1,89,50,12),_RlBrgMacSwAdminTrapFrequency_Type())
rlBrgMacSwAdminTrapFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:rlBrgMacSwAdminTrapFrequency.setStatus(_A)
mibBuilder.exportSymbols('RADLAN-BRGMACSWITCH-MIB',**{'rlBrgMacSwitch':rlBrgMacSwitch,'rlBrgMacSwVersion':rlBrgMacSwVersion,'rlBrgMacSwMaxTableNumber':rlBrgMacSwMaxTableNumber,'rlBrgMacSwDynamicTables':rlBrgMacSwDynamicTables,'rlBrgMacSwOldEntryDeleteMode':rlBrgMacSwOldEntryDeleteMode,'rlBrgMacSwSpanningTree':rlBrgMacSwSpanningTree,'rlBrgMacSwKeyType':rlBrgMacSwKeyType,'rlBrgMacSwYellowBoundary':rlBrgMacSwYellowBoundary,'rlBrgMacSwRedBoundary':rlBrgMacSwRedBoundary,'rlBrgMacSwTrapEnable':rlBrgMacSwTrapEnable,'rlBrgMacSwOperTrapCount':rlBrgMacSwOperTrapCount,'rlBrgMacSwAdminTrapFrequency':rlBrgMacSwAdminTrapFrequency})