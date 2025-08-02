_J='brcdHqosStatsPriority'
_I='brcdHqosEndpointInnerTag'
_H='brcdHqosEndpointTag'
_G='brcdHqosEndpointType'
_F='brcdHqosIfIndex'
_E='Integer32'
_D='not-accessible'
_C='BROCADE-QOS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
brcdQos,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','brcdQos')
PortPriorityTC,=mibBuilder.importSymbols('FOUNDRY-SN-SWITCH-GROUP-MIB','PortPriorityTC')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
brcdQosMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,1,14,1))
if mibBuilder.loadTexts:brcdQosMIB.setRevisions(('2012-07-18 00:00',))
_BrcdHqosObjects_ObjectIdentity=ObjectIdentity
brcdHqosObjects=_BrcdHqosObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,14,1,1))
_BrcdHqosStatsTable_Object=MibTable
brcdHqosStatsTable=_BrcdHqosStatsTable_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1))
if mibBuilder.loadTexts:brcdHqosStatsTable.setStatus(_A)
_BrcdHqosStatsEntry_Object=MibTableRow
brcdHqosStatsEntry=_BrcdHqosStatsEntry_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1))
brcdHqosStatsEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_H),(0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:brcdHqosStatsEntry.setStatus(_A)
_BrcdHqosIfIndex_Type=InterfaceIndex
_BrcdHqosIfIndex_Object=MibTableColumn
brcdHqosIfIndex=_BrcdHqosIfIndex_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1,1),_BrcdHqosIfIndex_Type())
brcdHqosIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdHqosIfIndex.setStatus(_A)
class _BrcdHqosEndpointType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('singleTaggedVlan',2),('doubleTaggedVlan',3),('bVlanIsid',4)))
_BrcdHqosEndpointType_Type.__name__=_E
_BrcdHqosEndpointType_Object=MibTableColumn
brcdHqosEndpointType=_BrcdHqosEndpointType_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1,2),_BrcdHqosEndpointType_Type())
brcdHqosEndpointType.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdHqosEndpointType.setStatus(_A)
_BrcdHqosEndpointTag_Type=Unsigned32
_BrcdHqosEndpointTag_Object=MibTableColumn
brcdHqosEndpointTag=_BrcdHqosEndpointTag_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1,3),_BrcdHqosEndpointTag_Type())
brcdHqosEndpointTag.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdHqosEndpointTag.setStatus(_A)
_BrcdHqosEndpointInnerTag_Type=Unsigned32
_BrcdHqosEndpointInnerTag_Object=MibTableColumn
brcdHqosEndpointInnerTag=_BrcdHqosEndpointInnerTag_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1,4),_BrcdHqosEndpointInnerTag_Type())
brcdHqosEndpointInnerTag.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdHqosEndpointInnerTag.setStatus(_A)
_BrcdHqosStatsPriority_Type=PortPriorityTC
_BrcdHqosStatsPriority_Object=MibTableColumn
brcdHqosStatsPriority=_BrcdHqosStatsPriority_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1,5),_BrcdHqosStatsPriority_Type())
brcdHqosStatsPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdHqosStatsPriority.setStatus(_A)
_BrcdHqosStatsDescription_Type=DisplayString
_BrcdHqosStatsDescription_Object=MibTableColumn
brcdHqosStatsDescription=_BrcdHqosStatsDescription_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1,6),_BrcdHqosStatsDescription_Type())
brcdHqosStatsDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdHqosStatsDescription.setStatus(_A)
_BrcdHqosStatsEnquePkts_Type=Counter64
_BrcdHqosStatsEnquePkts_Object=MibTableColumn
brcdHqosStatsEnquePkts=_BrcdHqosStatsEnquePkts_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1,7),_BrcdHqosStatsEnquePkts_Type())
brcdHqosStatsEnquePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdHqosStatsEnquePkts.setStatus(_A)
_BrcdHqosStatsEnqueBytes_Type=Counter64
_BrcdHqosStatsEnqueBytes_Object=MibTableColumn
brcdHqosStatsEnqueBytes=_BrcdHqosStatsEnqueBytes_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1,8),_BrcdHqosStatsEnqueBytes_Type())
brcdHqosStatsEnqueBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdHqosStatsEnqueBytes.setStatus(_A)
_BrcdHqosStatsDequePkts_Type=Counter64
_BrcdHqosStatsDequePkts_Object=MibTableColumn
brcdHqosStatsDequePkts=_BrcdHqosStatsDequePkts_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1,9),_BrcdHqosStatsDequePkts_Type())
brcdHqosStatsDequePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdHqosStatsDequePkts.setStatus(_A)
_BrcdHqosStatsDequeBytes_Type=Counter64
_BrcdHqosStatsDequeBytes_Object=MibTableColumn
brcdHqosStatsDequeBytes=_BrcdHqosStatsDequeBytes_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1,10),_BrcdHqosStatsDequeBytes_Type())
brcdHqosStatsDequeBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdHqosStatsDequeBytes.setStatus(_A)
_BrcdHqosStatsTotalDiscardPkts_Type=Counter64
_BrcdHqosStatsTotalDiscardPkts_Object=MibTableColumn
brcdHqosStatsTotalDiscardPkts=_BrcdHqosStatsTotalDiscardPkts_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1,11),_BrcdHqosStatsTotalDiscardPkts_Type())
brcdHqosStatsTotalDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdHqosStatsTotalDiscardPkts.setStatus(_A)
_BrcdHqosStatsTotalDiscardBytes_Type=Counter64
_BrcdHqosStatsTotalDiscardBytes_Object=MibTableColumn
brcdHqosStatsTotalDiscardBytes=_BrcdHqosStatsTotalDiscardBytes_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1,12),_BrcdHqosStatsTotalDiscardBytes_Type())
brcdHqosStatsTotalDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdHqosStatsTotalDiscardBytes.setStatus(_A)
_BrcdHqosStatsOldestDiscardPkts_Type=Counter64
_BrcdHqosStatsOldestDiscardPkts_Object=MibTableColumn
brcdHqosStatsOldestDiscardPkts=_BrcdHqosStatsOldestDiscardPkts_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1,13),_BrcdHqosStatsOldestDiscardPkts_Type())
brcdHqosStatsOldestDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdHqosStatsOldestDiscardPkts.setStatus(_A)
_BrcdHqosStatsOldestDiscardBytes_Type=Counter64
_BrcdHqosStatsOldestDiscardBytes_Object=MibTableColumn
brcdHqosStatsOldestDiscardBytes=_BrcdHqosStatsOldestDiscardBytes_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1,14),_BrcdHqosStatsOldestDiscardBytes_Type())
brcdHqosStatsOldestDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdHqosStatsOldestDiscardBytes.setStatus(_A)
_BrcdHqosStatsWREDDroppedPkts_Type=Counter64
_BrcdHqosStatsWREDDroppedPkts_Object=MibTableColumn
brcdHqosStatsWREDDroppedPkts=_BrcdHqosStatsWREDDroppedPkts_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1,15),_BrcdHqosStatsWREDDroppedPkts_Type())
brcdHqosStatsWREDDroppedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdHqosStatsWREDDroppedPkts.setStatus(_A)
_BrcdHqosStatsWREDDroppedBytes_Type=Counter64
_BrcdHqosStatsWREDDroppedBytes_Object=MibTableColumn
brcdHqosStatsWREDDroppedBytes=_BrcdHqosStatsWREDDroppedBytes_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1,16),_BrcdHqosStatsWREDDroppedBytes_Type())
brcdHqosStatsWREDDroppedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdHqosStatsWREDDroppedBytes.setStatus(_A)
_BrcdHqosStatsCurrentQDepth_Type=Counter64
_BrcdHqosStatsCurrentQDepth_Object=MibTableColumn
brcdHqosStatsCurrentQDepth=_BrcdHqosStatsCurrentQDepth_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1,17),_BrcdHqosStatsCurrentQDepth_Type())
brcdHqosStatsCurrentQDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdHqosStatsCurrentQDepth.setStatus(_A)
_BrcdHqosStatsMaxQDepthSinceLastRead_Type=Counter64
_BrcdHqosStatsMaxQDepthSinceLastRead_Object=MibTableColumn
brcdHqosStatsMaxQDepthSinceLastRead=_BrcdHqosStatsMaxQDepthSinceLastRead_Object((1,3,6,1,4,1,1991,1,1,14,1,1,1,1,18),_BrcdHqosStatsMaxQDepthSinceLastRead_Type())
brcdHqosStatsMaxQDepthSinceLastRead.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdHqosStatsMaxQDepthSinceLastRead.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'brcdQosMIB':brcdQosMIB,'brcdHqosObjects':brcdHqosObjects,'brcdHqosStatsTable':brcdHqosStatsTable,'brcdHqosStatsEntry':brcdHqosStatsEntry,_F:brcdHqosIfIndex,_G:brcdHqosEndpointType,_H:brcdHqosEndpointTag,_I:brcdHqosEndpointInnerTag,_J:brcdHqosStatsPriority,'brcdHqosStatsDescription':brcdHqosStatsDescription,'brcdHqosStatsEnquePkts':brcdHqosStatsEnquePkts,'brcdHqosStatsEnqueBytes':brcdHqosStatsEnqueBytes,'brcdHqosStatsDequePkts':brcdHqosStatsDequePkts,'brcdHqosStatsDequeBytes':brcdHqosStatsDequeBytes,'brcdHqosStatsTotalDiscardPkts':brcdHqosStatsTotalDiscardPkts,'brcdHqosStatsTotalDiscardBytes':brcdHqosStatsTotalDiscardBytes,'brcdHqosStatsOldestDiscardPkts':brcdHqosStatsOldestDiscardPkts,'brcdHqosStatsOldestDiscardBytes':brcdHqosStatsOldestDiscardBytes,'brcdHqosStatsWREDDroppedPkts':brcdHqosStatsWREDDroppedPkts,'brcdHqosStatsWREDDroppedBytes':brcdHqosStatsWREDDroppedBytes,'brcdHqosStatsCurrentQDepth':brcdHqosStatsCurrentQDepth,'brcdHqosStatsMaxQDepthSinceLastRead':brcdHqosStatsMaxQDepthSinceLastRead})