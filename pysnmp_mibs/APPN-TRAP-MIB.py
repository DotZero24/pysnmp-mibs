_i='appnTrapMibDlurNotifGroup'
_h='appnTrapMibDlurConfGroup'
_g='appnTrapMibTopoNotifGroup'
_f='appnTrapMibTopoConfGroup'
_e='appnTrapMibIsrNotifGroup'
_d='appnIsrAccountingDataTrap'
_c='appnPortOperState'
_b='appnLsOperState'
_a='appnLocalTgOperational'
_Z='appnLocalTgCpCpSession'
_Y='appnIsInSessUpTime'
_X='appnIsInS2PNonFmdPius'
_W='appnIsInS2PNonFmdBytes'
_V='appnIsInS2PFmdPius'
_U='appnIsInS2PFmdBytes'
_T='appnIsInP2SNonFmdPius'
_S='appnIsInP2SNonFmdBytes'
_R='appnIsInP2SFmdPius'
_Q='appnIsInP2SFmdBytes'
_P='dlurDlusSessnStatus'
_O='APPN-DLUR-MIB'
_N='dlurDlusTableChanges'
_M='appnLsTableChanges'
_L='appnPortTableChanges'
_K='appnTrapControl'
_J='dlurDlusStateChangeTrap'
_I='appnLsOperStateChangeTrap'
_H='appnPortOperStateChangeTrap'
_G='appnLocalTgCpCpChangeTrap'
_F='appnLocalTgOperStateChangeTrap'
_E='appnLocalTgTableChanges'
_D='read-only'
_C='APPN-MIB'
_B='current'
_A='APPN-TRAP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlurDlusSessnStatus,=mibBuilder.importSymbols(_O,_P)
appnCompliances,appnGroups,appnIsInP2SFmdBytes,appnIsInP2SFmdPius,appnIsInP2SNonFmdBytes,appnIsInP2SNonFmdPius,appnIsInS2PFmdBytes,appnIsInS2PFmdPius,appnIsInS2PNonFmdBytes,appnIsInS2PNonFmdPius,appnIsInSessUpTime,appnLocalTgCpCpSession,appnLocalTgOperational,appnLsOperState,appnMIB,appnObjects,appnPortOperState=mibBuilder.importSymbols(_C,'appnCompliances','appnGroups',_Q,_R,_S,_T,_U,_V,_W,_X,_Y,_Z,_a,_b,'appnMIB','appnObjects',_c)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
appnTrapMIB=ModuleIdentity((1,3,6,1,2,1,34,4,0))
_AppnTrapObjects_ObjectIdentity=ObjectIdentity
appnTrapObjects=_AppnTrapObjects_ObjectIdentity((1,3,6,1,2,1,34,4,1,7))
class _AppnTrapControl_Type(Bits):namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4)))
_AppnTrapControl_Type.__name__='Bits'
_AppnTrapControl_Object=MibScalar
appnTrapControl=_AppnTrapControl_Object((1,3,6,1,2,1,34,4,1,7,1),_AppnTrapControl_Type())
appnTrapControl.setMaxAccess('read-write')
if mibBuilder.loadTexts:appnTrapControl.setStatus(_B)
_AppnLocalTgTableChanges_Type=Counter32
_AppnLocalTgTableChanges_Object=MibScalar
appnLocalTgTableChanges=_AppnLocalTgTableChanges_Object((1,3,6,1,2,1,34,4,1,7,2),_AppnLocalTgTableChanges_Type())
appnLocalTgTableChanges.setMaxAccess(_D)
if mibBuilder.loadTexts:appnLocalTgTableChanges.setStatus(_B)
_AppnPortTableChanges_Type=Counter32
_AppnPortTableChanges_Object=MibScalar
appnPortTableChanges=_AppnPortTableChanges_Object((1,3,6,1,2,1,34,4,1,7,3),_AppnPortTableChanges_Type())
appnPortTableChanges.setMaxAccess(_D)
if mibBuilder.loadTexts:appnPortTableChanges.setStatus(_B)
_AppnLsTableChanges_Type=Counter32
_AppnLsTableChanges_Object=MibScalar
appnLsTableChanges=_AppnLsTableChanges_Object((1,3,6,1,2,1,34,4,1,7,4),_AppnLsTableChanges_Type())
appnLsTableChanges.setMaxAccess(_D)
if mibBuilder.loadTexts:appnLsTableChanges.setStatus(_B)
_DlurDlusTableChanges_Type=Counter32
_DlurDlusTableChanges_Object=MibScalar
dlurDlusTableChanges=_DlurDlusTableChanges_Object((1,3,6,1,2,1,34,4,1,7,5),_DlurDlusTableChanges_Type())
dlurDlusTableChanges.setMaxAccess(_D)
if mibBuilder.loadTexts:dlurDlusTableChanges.setStatus(_B)
appnTrapMibTopoConfGroup=ObjectGroup((1,3,6,1,2,1,34,4,3,2,22))
appnTrapMibTopoConfGroup.setObjects(*((_A,_K),(_A,_E),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:appnTrapMibTopoConfGroup.setStatus(_B)
appnTrapMibDlurConfGroup=ObjectGroup((1,3,6,1,2,1,34,4,3,2,24))
appnTrapMibDlurConfGroup.setObjects(*((_A,_K),(_A,_N)))
if mibBuilder.loadTexts:appnTrapMibDlurConfGroup.setStatus(_B)
appnIsrAccountingDataTrap=NotificationType((1,3,6,1,2,1,34,4,0,1))
appnIsrAccountingDataTrap.setObjects(*((_C,_R),(_C,_V),(_C,_T),(_C,_X),(_C,_Q),(_C,_U),(_C,_S),(_C,_W),(_C,_Y)))
if mibBuilder.loadTexts:appnIsrAccountingDataTrap.setStatus(_B)
appnLocalTgOperStateChangeTrap=NotificationType((1,3,6,1,2,1,34,4,0,2))
appnLocalTgOperStateChangeTrap.setObjects(*((_A,_E),(_C,_a)))
if mibBuilder.loadTexts:appnLocalTgOperStateChangeTrap.setStatus(_B)
appnLocalTgCpCpChangeTrap=NotificationType((1,3,6,1,2,1,34,4,0,3))
appnLocalTgCpCpChangeTrap.setObjects(*((_A,_E),(_C,_Z)))
if mibBuilder.loadTexts:appnLocalTgCpCpChangeTrap.setStatus(_B)
appnPortOperStateChangeTrap=NotificationType((1,3,6,1,2,1,34,4,0,4))
appnPortOperStateChangeTrap.setObjects(*((_A,_L),(_C,_c)))
if mibBuilder.loadTexts:appnPortOperStateChangeTrap.setStatus(_B)
appnLsOperStateChangeTrap=NotificationType((1,3,6,1,2,1,34,4,0,5))
appnLsOperStateChangeTrap.setObjects(*((_A,_M),(_C,_b)))
if mibBuilder.loadTexts:appnLsOperStateChangeTrap.setStatus(_B)
dlurDlusStateChangeTrap=NotificationType((1,3,6,1,2,1,34,4,0,6))
dlurDlusStateChangeTrap.setObjects(*((_A,_N),(_O,_P)))
if mibBuilder.loadTexts:dlurDlusStateChangeTrap.setStatus(_B)
appnTrapMibIsrNotifGroup=NotificationGroup((1,3,6,1,2,1,34,4,3,2,21))
appnTrapMibIsrNotifGroup.setObjects((_A,_d))
if mibBuilder.loadTexts:appnTrapMibIsrNotifGroup.setStatus(_B)
appnTrapMibTopoNotifGroup=NotificationGroup((1,3,6,1,2,1,34,4,3,2,23))
appnTrapMibTopoNotifGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:appnTrapMibTopoNotifGroup.setStatus(_B)
appnTrapMibDlurNotifGroup=NotificationGroup((1,3,6,1,2,1,34,4,3,2,25))
appnTrapMibDlurNotifGroup.setObjects((_A,_J))
if mibBuilder.loadTexts:appnTrapMibDlurNotifGroup.setStatus(_B)
appnTrapMibCompliance=ModuleCompliance((1,3,6,1,2,1,34,4,3,1,2))
appnTrapMibCompliance.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:appnTrapMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'appnTrapMIB':appnTrapMIB,_d:appnIsrAccountingDataTrap,_F:appnLocalTgOperStateChangeTrap,_G:appnLocalTgCpCpChangeTrap,_H:appnPortOperStateChangeTrap,_I:appnLsOperStateChangeTrap,_J:dlurDlusStateChangeTrap,'appnTrapObjects':appnTrapObjects,_K:appnTrapControl,_E:appnLocalTgTableChanges,_L:appnPortTableChanges,_M:appnLsTableChanges,_N:dlurDlusTableChanges,'appnTrapMibCompliance':appnTrapMibCompliance,_e:appnTrapMibIsrNotifGroup,_f:appnTrapMibTopoConfGroup,_g:appnTrapMibTopoNotifGroup,_h:appnTrapMibDlurConfGroup,_i:appnTrapMibDlurNotifGroup})