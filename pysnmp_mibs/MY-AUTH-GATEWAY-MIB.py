_X='myAuthGatewayMIBGroup'
_W='userStatus'
_V='overseasFluxCountDownlink'
_U='overseasFluxCountUplink'
_T='inlandFluxCountDownlink'
_S='inlandFluxCountUplink'
_R='intramuralFluxCountDownlink'
_Q='intramuralFluxCountUplink'
_P='overseasFluxLimitDownlink'
_O='overseasFluxLimitUplink'
_N='inlandFluxLimitDownlink'
_M='inlandFluxLimitUplink'
_L='intramuralFluxLimitDownlink'
_K='intramuralFluxLimitUplink'
_J='bandwidthLimitDownlink'
_I='bandwidthLimitUplink'
_H='timeUsed'
_G='timeLimit'
_F='onlineFlag'
_E='userIpaddr'
_D='read-write'
_C='read-only'
_B='MY-AUTH-GATEWAY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ip,=mibBuilder.importSymbols('IP-MIB','ip')
myMgmt,=mibBuilder.importSymbols('MY-SMI','myMgmt')
IfIndex,=mibBuilder.importSymbols('MY-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
myAuthGatewayMIB=ModuleIdentity((1,3,6,1,4,1,4881,1,1,10,2,40))
if mibBuilder.loadTexts:myAuthGatewayMIB.setRevisions(('2002-03-20 00:00',))
_MyAuthGatewayMIBObjects_ObjectIdentity=ObjectIdentity
myAuthGatewayMIBObjects=_MyAuthGatewayMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,40,1))
_MyAuthGatewayUserTable_Object=MibTable
myAuthGatewayUserTable=_MyAuthGatewayUserTable_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1))
if mibBuilder.loadTexts:myAuthGatewayUserTable.setStatus(_A)
_MyAuthGatewayUserEntry_Object=MibTableRow
myAuthGatewayUserEntry=_MyAuthGatewayUserEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1))
myAuthGatewayUserEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:myAuthGatewayUserEntry.setStatus(_A)
_UserIpaddr_Type=IpAddress
_UserIpaddr_Object=MibTableColumn
userIpaddr=_UserIpaddr_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,1),_UserIpaddr_Type())
userIpaddr.setMaxAccess(_C)
if mibBuilder.loadTexts:userIpaddr.setStatus(_A)
_OnlineFlag_Type=Gauge32
_OnlineFlag_Object=MibTableColumn
onlineFlag=_OnlineFlag_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,2),_OnlineFlag_Type())
onlineFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:onlineFlag.setStatus(_A)
_TimeLimit_Type=Gauge32
_TimeLimit_Object=MibTableColumn
timeLimit=_TimeLimit_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,3),_TimeLimit_Type())
timeLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:timeLimit.setStatus(_A)
_TimeUsed_Type=Gauge32
_TimeUsed_Object=MibTableColumn
timeUsed=_TimeUsed_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,4),_TimeUsed_Type())
timeUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:timeUsed.setStatus(_A)
_BandwidthLimitUplink_Type=Gauge32
_BandwidthLimitUplink_Object=MibTableColumn
bandwidthLimitUplink=_BandwidthLimitUplink_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,5),_BandwidthLimitUplink_Type())
bandwidthLimitUplink.setMaxAccess(_D)
if mibBuilder.loadTexts:bandwidthLimitUplink.setStatus(_A)
_BandwidthLimitDownlink_Type=Gauge32
_BandwidthLimitDownlink_Object=MibTableColumn
bandwidthLimitDownlink=_BandwidthLimitDownlink_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,6),_BandwidthLimitDownlink_Type())
bandwidthLimitDownlink.setMaxAccess(_D)
if mibBuilder.loadTexts:bandwidthLimitDownlink.setStatus(_A)
_IntramuralFluxLimitUplink_Type=Gauge32
_IntramuralFluxLimitUplink_Object=MibTableColumn
intramuralFluxLimitUplink=_IntramuralFluxLimitUplink_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,7),_IntramuralFluxLimitUplink_Type())
intramuralFluxLimitUplink.setMaxAccess(_D)
if mibBuilder.loadTexts:intramuralFluxLimitUplink.setStatus(_A)
_IntramuralFluxLimitDownlink_Type=Gauge32
_IntramuralFluxLimitDownlink_Object=MibTableColumn
intramuralFluxLimitDownlink=_IntramuralFluxLimitDownlink_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,8),_IntramuralFluxLimitDownlink_Type())
intramuralFluxLimitDownlink.setMaxAccess(_D)
if mibBuilder.loadTexts:intramuralFluxLimitDownlink.setStatus(_A)
_InlandFluxLimitUplink_Type=Gauge32
_InlandFluxLimitUplink_Object=MibTableColumn
inlandFluxLimitUplink=_InlandFluxLimitUplink_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,9),_InlandFluxLimitUplink_Type())
inlandFluxLimitUplink.setMaxAccess(_D)
if mibBuilder.loadTexts:inlandFluxLimitUplink.setStatus(_A)
_InlandFluxLimitDownlink_Type=Gauge32
_InlandFluxLimitDownlink_Object=MibTableColumn
inlandFluxLimitDownlink=_InlandFluxLimitDownlink_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,10),_InlandFluxLimitDownlink_Type())
inlandFluxLimitDownlink.setMaxAccess(_D)
if mibBuilder.loadTexts:inlandFluxLimitDownlink.setStatus(_A)
_OverseasFluxLimitUplink_Type=Gauge32
_OverseasFluxLimitUplink_Object=MibTableColumn
overseasFluxLimitUplink=_OverseasFluxLimitUplink_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,11),_OverseasFluxLimitUplink_Type())
overseasFluxLimitUplink.setMaxAccess(_D)
if mibBuilder.loadTexts:overseasFluxLimitUplink.setStatus(_A)
_OverseasFluxLimitDownlink_Type=Gauge32
_OverseasFluxLimitDownlink_Object=MibTableColumn
overseasFluxLimitDownlink=_OverseasFluxLimitDownlink_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,12),_OverseasFluxLimitDownlink_Type())
overseasFluxLimitDownlink.setMaxAccess(_D)
if mibBuilder.loadTexts:overseasFluxLimitDownlink.setStatus(_A)
_IntramuralFluxCountUplink_Type=Counter32
_IntramuralFluxCountUplink_Object=MibTableColumn
intramuralFluxCountUplink=_IntramuralFluxCountUplink_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,13),_IntramuralFluxCountUplink_Type())
intramuralFluxCountUplink.setMaxAccess(_C)
if mibBuilder.loadTexts:intramuralFluxCountUplink.setStatus(_A)
_IntramuralFluxCountDownlink_Type=Counter32
_IntramuralFluxCountDownlink_Object=MibTableColumn
intramuralFluxCountDownlink=_IntramuralFluxCountDownlink_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,14),_IntramuralFluxCountDownlink_Type())
intramuralFluxCountDownlink.setMaxAccess(_C)
if mibBuilder.loadTexts:intramuralFluxCountDownlink.setStatus(_A)
_InlandFluxCountUplink_Type=Counter32
_InlandFluxCountUplink_Object=MibTableColumn
inlandFluxCountUplink=_InlandFluxCountUplink_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,15),_InlandFluxCountUplink_Type())
inlandFluxCountUplink.setMaxAccess(_C)
if mibBuilder.loadTexts:inlandFluxCountUplink.setStatus(_A)
_InlandFluxCountDownlink_Type=Counter32
_InlandFluxCountDownlink_Object=MibTableColumn
inlandFluxCountDownlink=_InlandFluxCountDownlink_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,16),_InlandFluxCountDownlink_Type())
inlandFluxCountDownlink.setMaxAccess(_C)
if mibBuilder.loadTexts:inlandFluxCountDownlink.setStatus(_A)
_OverseasFluxCountUplink_Type=Counter32
_OverseasFluxCountUplink_Object=MibTableColumn
overseasFluxCountUplink=_OverseasFluxCountUplink_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,17),_OverseasFluxCountUplink_Type())
overseasFluxCountUplink.setMaxAccess(_C)
if mibBuilder.loadTexts:overseasFluxCountUplink.setStatus(_A)
_OverseasFluxCountDownlink_Type=Counter32
_OverseasFluxCountDownlink_Object=MibTableColumn
overseasFluxCountDownlink=_OverseasFluxCountDownlink_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,18),_OverseasFluxCountDownlink_Type())
overseasFluxCountDownlink.setMaxAccess(_C)
if mibBuilder.loadTexts:overseasFluxCountDownlink.setStatus(_A)
_UserStatus_Type=RowStatus
_UserStatus_Object=MibTableColumn
userStatus=_UserStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,40,1,1,1,19),_UserStatus_Type())
userStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:userStatus.setStatus(_A)
_MyAuthGatewayMIBTraps_ObjectIdentity=ObjectIdentity
myAuthGatewayMIBTraps=_MyAuthGatewayMIBTraps_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,40,2))
_MyAuthGatewayMIBConformance_ObjectIdentity=ObjectIdentity
myAuthGatewayMIBConformance=_MyAuthGatewayMIBConformance_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,40,3))
_MyAuthGatewayMIBCompliances_ObjectIdentity=ObjectIdentity
myAuthGatewayMIBCompliances=_MyAuthGatewayMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,40,3,1))
_MyAuthGatewayMIBGroups_ObjectIdentity=ObjectIdentity
myAuthGatewayMIBGroups=_MyAuthGatewayMIBGroups_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,40,3,2))
myAuthGatewayMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,40,3,2,1))
myAuthGatewayMIBGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:myAuthGatewayMIBGroup.setStatus(_A)
myAuthGatewayUserLeave=NotificationType((1,3,6,1,4,1,4881,1,1,10,2,40,2,1))
myAuthGatewayUserLeave.setObjects((_B,_E))
if mibBuilder.loadTexts:myAuthGatewayUserLeave.setStatus(_A)
myAuthGatewayMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4881,1,1,10,2,40,3,1,1))
myAuthGatewayMIBCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:myAuthGatewayMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myAuthGatewayMIB':myAuthGatewayMIB,'myAuthGatewayMIBObjects':myAuthGatewayMIBObjects,'myAuthGatewayUserTable':myAuthGatewayUserTable,'myAuthGatewayUserEntry':myAuthGatewayUserEntry,_E:userIpaddr,_F:onlineFlag,_G:timeLimit,_H:timeUsed,_I:bandwidthLimitUplink,_J:bandwidthLimitDownlink,_K:intramuralFluxLimitUplink,_L:intramuralFluxLimitDownlink,_M:inlandFluxLimitUplink,_N:inlandFluxLimitDownlink,_O:overseasFluxLimitUplink,_P:overseasFluxLimitDownlink,_Q:intramuralFluxCountUplink,_R:intramuralFluxCountDownlink,_S:inlandFluxCountUplink,_T:inlandFluxCountDownlink,_U:overseasFluxCountUplink,_V:overseasFluxCountDownlink,_W:userStatus,'myAuthGatewayMIBTraps':myAuthGatewayMIBTraps,'myAuthGatewayUserLeave':myAuthGatewayUserLeave,'myAuthGatewayMIBConformance':myAuthGatewayMIBConformance,'myAuthGatewayMIBCompliances':myAuthGatewayMIBCompliances,'myAuthGatewayMIBCompliance':myAuthGatewayMIBCompliance,'myAuthGatewayMIBGroups':myAuthGatewayMIBGroups,_X:myAuthGatewayMIBGroup})