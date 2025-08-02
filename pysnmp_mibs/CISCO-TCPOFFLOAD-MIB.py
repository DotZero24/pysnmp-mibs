_U='ciscoTcpOffloadGroup'
_T='cipCardOffloadConfigRowStatus'
_S='cipCardOffloadConfigBroadcastEnable'
_R='cipCardOffloadConfigAPIRouterAppl'
_Q='cipCardOffloadConfigAPIHostAppl'
_P='cipCardOffloadConfigLinkRouterAppl'
_O='cipCardOffloadConfigLinkHostAppl'
_N='cipCardOffloadConfigRouterName'
_M='cipCardOffloadConfigHostName'
_L='cipCardOffloadConfigIpAddr'
_K='cipCardOffloadConfigDevice'
_J='cipCardOffloadConfigPath'
_I='cipCardSubChannelIndex'
_H='cipCardEntryIndex'
_G='cipCardDtrBrdIndex'
_F='OctetString'
_E='CISCO-CHANNEL-MIB'
_D='DisplayString'
_C='read-create'
_B='CISCO-TCPOFFLOAD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cipCardDtrBrdIndex,cipCardEntryIndex,cipCardSubChannelIndex=mibBuilder.importSymbols(_E,_G,_H,_I)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention','TruthValue')
ciscoTcpOffloadMIB=ModuleIdentity((1,3,6,1,4,1,9,9,31))
if mibBuilder.loadTexts:ciscoTcpOffloadMIB.setRevisions(('1998-01-06 00:00','1995-04-27 00:00'))
_TcpOffloadObjects_ObjectIdentity=ObjectIdentity
tcpOffloadObjects=_TcpOffloadObjects_ObjectIdentity((1,3,6,1,4,1,9,9,31,1))
_CipCardOffloadConfig_ObjectIdentity=ObjectIdentity
cipCardOffloadConfig=_CipCardOffloadConfig_ObjectIdentity((1,3,6,1,4,1,9,9,31,1,1))
_CipCardOffloadConfigTable_Object=MibTable
cipCardOffloadConfigTable=_CipCardOffloadConfigTable_Object((1,3,6,1,4,1,9,9,31,1,1,1))
if mibBuilder.loadTexts:cipCardOffloadConfigTable.setStatus(_A)
_CipCardOffloadConfigEntry_Object=MibTableRow
cipCardOffloadConfigEntry=_CipCardOffloadConfigEntry_Object((1,3,6,1,4,1,9,9,31,1,1,1,1))
cipCardOffloadConfigEntry.setIndexNames((0,_E,_H),(0,_E,_G),(0,_E,_I))
if mibBuilder.loadTexts:cipCardOffloadConfigEntry.setStatus(_A)
class _CipCardOffloadConfigPath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_CipCardOffloadConfigPath_Type.__name__=_F
_CipCardOffloadConfigPath_Object=MibTableColumn
cipCardOffloadConfigPath=_CipCardOffloadConfigPath_Object((1,3,6,1,4,1,9,9,31,1,1,1,1,1),_CipCardOffloadConfigPath_Type())
cipCardOffloadConfigPath.setMaxAccess(_C)
if mibBuilder.loadTexts:cipCardOffloadConfigPath.setStatus(_A)
class _CipCardOffloadConfigDevice_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_CipCardOffloadConfigDevice_Type.__name__=_F
_CipCardOffloadConfigDevice_Object=MibTableColumn
cipCardOffloadConfigDevice=_CipCardOffloadConfigDevice_Object((1,3,6,1,4,1,9,9,31,1,1,1,1,2),_CipCardOffloadConfigDevice_Type())
cipCardOffloadConfigDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:cipCardOffloadConfigDevice.setStatus(_A)
_CipCardOffloadConfigIpAddr_Type=IpAddress
_CipCardOffloadConfigIpAddr_Object=MibTableColumn
cipCardOffloadConfigIpAddr=_CipCardOffloadConfigIpAddr_Object((1,3,6,1,4,1,9,9,31,1,1,1,1,3),_CipCardOffloadConfigIpAddr_Type())
cipCardOffloadConfigIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cipCardOffloadConfigIpAddr.setStatus(_A)
class _CipCardOffloadConfigHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_CipCardOffloadConfigHostName_Type.__name__=_D
_CipCardOffloadConfigHostName_Object=MibTableColumn
cipCardOffloadConfigHostName=_CipCardOffloadConfigHostName_Object((1,3,6,1,4,1,9,9,31,1,1,1,1,4),_CipCardOffloadConfigHostName_Type())
cipCardOffloadConfigHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:cipCardOffloadConfigHostName.setStatus(_A)
class _CipCardOffloadConfigRouterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_CipCardOffloadConfigRouterName_Type.__name__=_D
_CipCardOffloadConfigRouterName_Object=MibTableColumn
cipCardOffloadConfigRouterName=_CipCardOffloadConfigRouterName_Object((1,3,6,1,4,1,9,9,31,1,1,1,1,5),_CipCardOffloadConfigRouterName_Type())
cipCardOffloadConfigRouterName.setMaxAccess(_C)
if mibBuilder.loadTexts:cipCardOffloadConfigRouterName.setStatus(_A)
class _CipCardOffloadConfigLinkHostAppl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_CipCardOffloadConfigLinkHostAppl_Type.__name__=_D
_CipCardOffloadConfigLinkHostAppl_Object=MibTableColumn
cipCardOffloadConfigLinkHostAppl=_CipCardOffloadConfigLinkHostAppl_Object((1,3,6,1,4,1,9,9,31,1,1,1,1,6),_CipCardOffloadConfigLinkHostAppl_Type())
cipCardOffloadConfigLinkHostAppl.setMaxAccess(_C)
if mibBuilder.loadTexts:cipCardOffloadConfigLinkHostAppl.setStatus(_A)
class _CipCardOffloadConfigLinkRouterAppl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_CipCardOffloadConfigLinkRouterAppl_Type.__name__=_D
_CipCardOffloadConfigLinkRouterAppl_Object=MibTableColumn
cipCardOffloadConfigLinkRouterAppl=_CipCardOffloadConfigLinkRouterAppl_Object((1,3,6,1,4,1,9,9,31,1,1,1,1,7),_CipCardOffloadConfigLinkRouterAppl_Type())
cipCardOffloadConfigLinkRouterAppl.setMaxAccess(_C)
if mibBuilder.loadTexts:cipCardOffloadConfigLinkRouterAppl.setStatus(_A)
class _CipCardOffloadConfigAPIHostAppl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_CipCardOffloadConfigAPIHostAppl_Type.__name__=_D
_CipCardOffloadConfigAPIHostAppl_Object=MibTableColumn
cipCardOffloadConfigAPIHostAppl=_CipCardOffloadConfigAPIHostAppl_Object((1,3,6,1,4,1,9,9,31,1,1,1,1,8),_CipCardOffloadConfigAPIHostAppl_Type())
cipCardOffloadConfigAPIHostAppl.setMaxAccess(_C)
if mibBuilder.loadTexts:cipCardOffloadConfigAPIHostAppl.setStatus(_A)
class _CipCardOffloadConfigAPIRouterAppl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_CipCardOffloadConfigAPIRouterAppl_Type.__name__=_D
_CipCardOffloadConfigAPIRouterAppl_Object=MibTableColumn
cipCardOffloadConfigAPIRouterAppl=_CipCardOffloadConfigAPIRouterAppl_Object((1,3,6,1,4,1,9,9,31,1,1,1,1,9),_CipCardOffloadConfigAPIRouterAppl_Type())
cipCardOffloadConfigAPIRouterAppl.setMaxAccess(_C)
if mibBuilder.loadTexts:cipCardOffloadConfigAPIRouterAppl.setStatus(_A)
_CipCardOffloadConfigBroadcastEnable_Type=TruthValue
_CipCardOffloadConfigBroadcastEnable_Object=MibTableColumn
cipCardOffloadConfigBroadcastEnable=_CipCardOffloadConfigBroadcastEnable_Object((1,3,6,1,4,1,9,9,31,1,1,1,1,10),_CipCardOffloadConfigBroadcastEnable_Type())
cipCardOffloadConfigBroadcastEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cipCardOffloadConfigBroadcastEnable.setStatus(_A)
_CipCardOffloadConfigRowStatus_Type=RowStatus
_CipCardOffloadConfigRowStatus_Object=MibTableColumn
cipCardOffloadConfigRowStatus=_CipCardOffloadConfigRowStatus_Object((1,3,6,1,4,1,9,9,31,1,1,1,1,11),_CipCardOffloadConfigRowStatus_Type())
cipCardOffloadConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cipCardOffloadConfigRowStatus.setStatus(_A)
_CiscoTcpOffloadMibConformance_ObjectIdentity=ObjectIdentity
ciscoTcpOffloadMibConformance=_CiscoTcpOffloadMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,31,2))
_CiscoTcpOffloadMibCompliances_ObjectIdentity=ObjectIdentity
ciscoTcpOffloadMibCompliances=_CiscoTcpOffloadMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,31,2,1))
_CiscoTcpOffloadMibGroups_ObjectIdentity=ObjectIdentity
ciscoTcpOffloadMibGroups=_CiscoTcpOffloadMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,31,2,2))
ciscoTcpOffloadGroup=ObjectGroup((1,3,6,1,4,1,9,9,31,2,2,1))
ciscoTcpOffloadGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ciscoTcpOffloadGroup.setStatus(_A)
ciscoTcpOffloadMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,31,2,1,1))
ciscoTcpOffloadMibCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:ciscoTcpOffloadMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoTcpOffloadMIB':ciscoTcpOffloadMIB,'tcpOffloadObjects':tcpOffloadObjects,'cipCardOffloadConfig':cipCardOffloadConfig,'cipCardOffloadConfigTable':cipCardOffloadConfigTable,'cipCardOffloadConfigEntry':cipCardOffloadConfigEntry,_J:cipCardOffloadConfigPath,_K:cipCardOffloadConfigDevice,_L:cipCardOffloadConfigIpAddr,_M:cipCardOffloadConfigHostName,_N:cipCardOffloadConfigRouterName,_O:cipCardOffloadConfigLinkHostAppl,_P:cipCardOffloadConfigLinkRouterAppl,_Q:cipCardOffloadConfigAPIHostAppl,_R:cipCardOffloadConfigAPIRouterAppl,_S:cipCardOffloadConfigBroadcastEnable,_T:cipCardOffloadConfigRowStatus,'ciscoTcpOffloadMibConformance':ciscoTcpOffloadMibConformance,'ciscoTcpOffloadMibCompliances':ciscoTcpOffloadMibCompliances,'ciscoTcpOffloadMibCompliance':ciscoTcpOffloadMibCompliance,'ciscoTcpOffloadMibGroups':ciscoTcpOffloadMibGroups,_U:ciscoTcpOffloadGroup})