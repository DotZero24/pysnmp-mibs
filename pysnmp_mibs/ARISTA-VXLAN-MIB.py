_m='aristaVxlanMibCountersGroup'
_l='aristaVxlanVtiVniEncapPkts'
_k='aristaVxlanVtiVniEncapBytes'
_j='aristaVxlanVtiVniDecapPkts'
_i='aristaVxlanVtiVniDecapBytes'
_h='aristaVxlanVniEncapDropPkts'
_g='aristaVxlanVniEncapBUMPkts'
_f='aristaVxlanVniEncapBUMBytes'
_e='aristaVxlanVniEncapPkts'
_d='aristaVxlanVniEncapBytes'
_c='aristaVxlanVniDecapDropExcptPkts'
_b='aristaVxlanVniDecapDropExcptBytes'
_a='aristaVxlanVniDecapBUMPkts'
_Z='aristaVxlanVniDecapBUMBytes'
_Y='aristaVxlanVniDecapKnownUcastPkts'
_X='aristaVxlanVniDecapKnownUcastBytes'
_W='aristaVxlanVniDecapPkts'
_V='aristaVxlanVniDecapBytes'
_U='aristaVxlanVtepEncapDropExcptPkts'
_T='aristaVxlanVtepEncapBUMPkts'
_S='aristaVxlanVtepEncapPkts'
_R='aristaVxlanVtepEncapBytes'
_Q='aristaVxlanVtepDecapDropExcptPkts'
_P='aristaVxlanVtepDecapDropExcptBytes'
_O='aristaVxlanVtepDecapBUMPkts'
_N='aristaVxlanVtepDecapBUMBytes'
_M='aristaVxlanVtepDecapKnownUcastPkts'
_L='aristaVxlanVtepDecapKnownUcastBytes'
_K='aristaVxlanVtepDecapPkts'
_J='aristaVxlanVtepDecapBytes'
_I='aristaVxlanVtiIndex'
_H='aristaVxlanVtepAddress'
_G='aristaVxlanVtepAddressType'
_F='InetAddress'
_E='aristaVxlanVni'
_D='not-accessible'
_C='read-only'
_B='ARISTA-VXLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_F,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
aristaVxlanMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,28))
if mibBuilder.loadTexts:aristaVxlanMIB.setRevisions(('2022-09-15 00:00','2020-06-01 00:00'))
_AristaVxlanMibNotifications_ObjectIdentity=ObjectIdentity
aristaVxlanMibNotifications=_AristaVxlanMibNotifications_ObjectIdentity((1,3,6,1,4,1,30065,3,28,0))
_AristaVxlanMibObjects_ObjectIdentity=ObjectIdentity
aristaVxlanMibObjects=_AristaVxlanMibObjects_ObjectIdentity((1,3,6,1,4,1,30065,3,28,1))
_AristaVxlanVtepCountersTable_Object=MibTable
aristaVxlanVtepCountersTable=_AristaVxlanVtepCountersTable_Object((1,3,6,1,4,1,30065,3,28,1,1))
if mibBuilder.loadTexts:aristaVxlanVtepCountersTable.setStatus(_A)
_AristaVxlanVtepCountersEntry_Object=MibTableRow
aristaVxlanVtepCountersEntry=_AristaVxlanVtepCountersEntry_Object((1,3,6,1,4,1,30065,3,28,1,1,1))
aristaVxlanVtepCountersEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:aristaVxlanVtepCountersEntry.setStatus(_A)
_AristaVxlanVtepAddressType_Type=InetAddressType
_AristaVxlanVtepAddressType_Object=MibTableColumn
aristaVxlanVtepAddressType=_AristaVxlanVtepAddressType_Object((1,3,6,1,4,1,30065,3,28,1,1,1,1),_AristaVxlanVtepAddressType_Type())
aristaVxlanVtepAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaVxlanVtepAddressType.setStatus(_A)
class _AristaVxlanVtepAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AristaVxlanVtepAddress_Type.__name__=_F
_AristaVxlanVtepAddress_Object=MibTableColumn
aristaVxlanVtepAddress=_AristaVxlanVtepAddress_Object((1,3,6,1,4,1,30065,3,28,1,1,1,2),_AristaVxlanVtepAddress_Type())
aristaVxlanVtepAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaVxlanVtepAddress.setStatus(_A)
_AristaVxlanVtepDecapBytes_Type=Counter64
_AristaVxlanVtepDecapBytes_Object=MibTableColumn
aristaVxlanVtepDecapBytes=_AristaVxlanVtepDecapBytes_Object((1,3,6,1,4,1,30065,3,28,1,1,1,3),_AristaVxlanVtepDecapBytes_Type())
aristaVxlanVtepDecapBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVtepDecapBytes.setStatus(_A)
_AristaVxlanVtepDecapPkts_Type=Counter64
_AristaVxlanVtepDecapPkts_Object=MibTableColumn
aristaVxlanVtepDecapPkts=_AristaVxlanVtepDecapPkts_Object((1,3,6,1,4,1,30065,3,28,1,1,1,4),_AristaVxlanVtepDecapPkts_Type())
aristaVxlanVtepDecapPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVtepDecapPkts.setStatus(_A)
_AristaVxlanVtepDecapKnownUcastBytes_Type=Counter64
_AristaVxlanVtepDecapKnownUcastBytes_Object=MibTableColumn
aristaVxlanVtepDecapKnownUcastBytes=_AristaVxlanVtepDecapKnownUcastBytes_Object((1,3,6,1,4,1,30065,3,28,1,1,1,5),_AristaVxlanVtepDecapKnownUcastBytes_Type())
aristaVxlanVtepDecapKnownUcastBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVtepDecapKnownUcastBytes.setStatus(_A)
_AristaVxlanVtepDecapKnownUcastPkts_Type=Counter64
_AristaVxlanVtepDecapKnownUcastPkts_Object=MibTableColumn
aristaVxlanVtepDecapKnownUcastPkts=_AristaVxlanVtepDecapKnownUcastPkts_Object((1,3,6,1,4,1,30065,3,28,1,1,1,6),_AristaVxlanVtepDecapKnownUcastPkts_Type())
aristaVxlanVtepDecapKnownUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVtepDecapKnownUcastPkts.setStatus(_A)
_AristaVxlanVtepDecapBUMBytes_Type=Counter64
_AristaVxlanVtepDecapBUMBytes_Object=MibTableColumn
aristaVxlanVtepDecapBUMBytes=_AristaVxlanVtepDecapBUMBytes_Object((1,3,6,1,4,1,30065,3,28,1,1,1,7),_AristaVxlanVtepDecapBUMBytes_Type())
aristaVxlanVtepDecapBUMBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVtepDecapBUMBytes.setStatus(_A)
_AristaVxlanVtepDecapBUMPkts_Type=Counter64
_AristaVxlanVtepDecapBUMPkts_Object=MibTableColumn
aristaVxlanVtepDecapBUMPkts=_AristaVxlanVtepDecapBUMPkts_Object((1,3,6,1,4,1,30065,3,28,1,1,1,8),_AristaVxlanVtepDecapBUMPkts_Type())
aristaVxlanVtepDecapBUMPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVtepDecapBUMPkts.setStatus(_A)
_AristaVxlanVtepDecapDropExcptBytes_Type=Counter64
_AristaVxlanVtepDecapDropExcptBytes_Object=MibTableColumn
aristaVxlanVtepDecapDropExcptBytes=_AristaVxlanVtepDecapDropExcptBytes_Object((1,3,6,1,4,1,30065,3,28,1,1,1,9),_AristaVxlanVtepDecapDropExcptBytes_Type())
aristaVxlanVtepDecapDropExcptBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVtepDecapDropExcptBytes.setStatus(_A)
_AristaVxlanVtepDecapDropExcptPkts_Type=Counter64
_AristaVxlanVtepDecapDropExcptPkts_Object=MibTableColumn
aristaVxlanVtepDecapDropExcptPkts=_AristaVxlanVtepDecapDropExcptPkts_Object((1,3,6,1,4,1,30065,3,28,1,1,1,10),_AristaVxlanVtepDecapDropExcptPkts_Type())
aristaVxlanVtepDecapDropExcptPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVtepDecapDropExcptPkts.setStatus(_A)
_AristaVxlanVtepEncapBytes_Type=Counter64
_AristaVxlanVtepEncapBytes_Object=MibTableColumn
aristaVxlanVtepEncapBytes=_AristaVxlanVtepEncapBytes_Object((1,3,6,1,4,1,30065,3,28,1,1,1,11),_AristaVxlanVtepEncapBytes_Type())
aristaVxlanVtepEncapBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVtepEncapBytes.setStatus(_A)
_AristaVxlanVtepEncapPkts_Type=Counter64
_AristaVxlanVtepEncapPkts_Object=MibTableColumn
aristaVxlanVtepEncapPkts=_AristaVxlanVtepEncapPkts_Object((1,3,6,1,4,1,30065,3,28,1,1,1,12),_AristaVxlanVtepEncapPkts_Type())
aristaVxlanVtepEncapPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVtepEncapPkts.setStatus(_A)
_AristaVxlanVtepEncapBUMPkts_Type=Counter64
_AristaVxlanVtepEncapBUMPkts_Object=MibTableColumn
aristaVxlanVtepEncapBUMPkts=_AristaVxlanVtepEncapBUMPkts_Object((1,3,6,1,4,1,30065,3,28,1,1,1,13),_AristaVxlanVtepEncapBUMPkts_Type())
aristaVxlanVtepEncapBUMPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVtepEncapBUMPkts.setStatus(_A)
_AristaVxlanVtepEncapDropExcptPkts_Type=Counter64
_AristaVxlanVtepEncapDropExcptPkts_Object=MibTableColumn
aristaVxlanVtepEncapDropExcptPkts=_AristaVxlanVtepEncapDropExcptPkts_Object((1,3,6,1,4,1,30065,3,28,1,1,1,14),_AristaVxlanVtepEncapDropExcptPkts_Type())
aristaVxlanVtepEncapDropExcptPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVtepEncapDropExcptPkts.setStatus(_A)
_AristaVxlanVniCountersTable_Object=MibTable
aristaVxlanVniCountersTable=_AristaVxlanVniCountersTable_Object((1,3,6,1,4,1,30065,3,28,1,2))
if mibBuilder.loadTexts:aristaVxlanVniCountersTable.setStatus(_A)
_AristaVxlanVniCountersEntry_Object=MibTableRow
aristaVxlanVniCountersEntry=_AristaVxlanVniCountersEntry_Object((1,3,6,1,4,1,30065,3,28,1,2,1))
aristaVxlanVniCountersEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:aristaVxlanVniCountersEntry.setStatus(_A)
_AristaVxlanVni_Type=Unsigned32
_AristaVxlanVni_Object=MibTableColumn
aristaVxlanVni=_AristaVxlanVni_Object((1,3,6,1,4,1,30065,3,28,1,2,1,1),_AristaVxlanVni_Type())
aristaVxlanVni.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaVxlanVni.setStatus(_A)
_AristaVxlanVniDecapBytes_Type=Counter64
_AristaVxlanVniDecapBytes_Object=MibTableColumn
aristaVxlanVniDecapBytes=_AristaVxlanVniDecapBytes_Object((1,3,6,1,4,1,30065,3,28,1,2,1,2),_AristaVxlanVniDecapBytes_Type())
aristaVxlanVniDecapBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVniDecapBytes.setStatus(_A)
_AristaVxlanVniDecapPkts_Type=Counter64
_AristaVxlanVniDecapPkts_Object=MibTableColumn
aristaVxlanVniDecapPkts=_AristaVxlanVniDecapPkts_Object((1,3,6,1,4,1,30065,3,28,1,2,1,3),_AristaVxlanVniDecapPkts_Type())
aristaVxlanVniDecapPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVniDecapPkts.setStatus(_A)
_AristaVxlanVniDecapKnownUcastBytes_Type=Counter64
_AristaVxlanVniDecapKnownUcastBytes_Object=MibTableColumn
aristaVxlanVniDecapKnownUcastBytes=_AristaVxlanVniDecapKnownUcastBytes_Object((1,3,6,1,4,1,30065,3,28,1,2,1,4),_AristaVxlanVniDecapKnownUcastBytes_Type())
aristaVxlanVniDecapKnownUcastBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVniDecapKnownUcastBytes.setStatus(_A)
_AristaVxlanVniDecapKnownUcastPkts_Type=Counter64
_AristaVxlanVniDecapKnownUcastPkts_Object=MibTableColumn
aristaVxlanVniDecapKnownUcastPkts=_AristaVxlanVniDecapKnownUcastPkts_Object((1,3,6,1,4,1,30065,3,28,1,2,1,5),_AristaVxlanVniDecapKnownUcastPkts_Type())
aristaVxlanVniDecapKnownUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVniDecapKnownUcastPkts.setStatus(_A)
_AristaVxlanVniDecapBUMBytes_Type=Counter64
_AristaVxlanVniDecapBUMBytes_Object=MibTableColumn
aristaVxlanVniDecapBUMBytes=_AristaVxlanVniDecapBUMBytes_Object((1,3,6,1,4,1,30065,3,28,1,2,1,6),_AristaVxlanVniDecapBUMBytes_Type())
aristaVxlanVniDecapBUMBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVniDecapBUMBytes.setStatus(_A)
_AristaVxlanVniDecapBUMPkts_Type=Counter64
_AristaVxlanVniDecapBUMPkts_Object=MibTableColumn
aristaVxlanVniDecapBUMPkts=_AristaVxlanVniDecapBUMPkts_Object((1,3,6,1,4,1,30065,3,28,1,2,1,7),_AristaVxlanVniDecapBUMPkts_Type())
aristaVxlanVniDecapBUMPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVniDecapBUMPkts.setStatus(_A)
_AristaVxlanVniDecapDropExcptBytes_Type=Counter64
_AristaVxlanVniDecapDropExcptBytes_Object=MibTableColumn
aristaVxlanVniDecapDropExcptBytes=_AristaVxlanVniDecapDropExcptBytes_Object((1,3,6,1,4,1,30065,3,28,1,2,1,8),_AristaVxlanVniDecapDropExcptBytes_Type())
aristaVxlanVniDecapDropExcptBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVniDecapDropExcptBytes.setStatus(_A)
_AristaVxlanVniDecapDropExcptPkts_Type=Counter64
_AristaVxlanVniDecapDropExcptPkts_Object=MibTableColumn
aristaVxlanVniDecapDropExcptPkts=_AristaVxlanVniDecapDropExcptPkts_Object((1,3,6,1,4,1,30065,3,28,1,2,1,9),_AristaVxlanVniDecapDropExcptPkts_Type())
aristaVxlanVniDecapDropExcptPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVniDecapDropExcptPkts.setStatus(_A)
_AristaVxlanVniEncapBytes_Type=Counter64
_AristaVxlanVniEncapBytes_Object=MibTableColumn
aristaVxlanVniEncapBytes=_AristaVxlanVniEncapBytes_Object((1,3,6,1,4,1,30065,3,28,1,2,1,10),_AristaVxlanVniEncapBytes_Type())
aristaVxlanVniEncapBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVniEncapBytes.setStatus(_A)
_AristaVxlanVniEncapPkts_Type=Counter64
_AristaVxlanVniEncapPkts_Object=MibTableColumn
aristaVxlanVniEncapPkts=_AristaVxlanVniEncapPkts_Object((1,3,6,1,4,1,30065,3,28,1,2,1,11),_AristaVxlanVniEncapPkts_Type())
aristaVxlanVniEncapPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVniEncapPkts.setStatus(_A)
_AristaVxlanVniEncapBUMBytes_Type=Counter64
_AristaVxlanVniEncapBUMBytes_Object=MibTableColumn
aristaVxlanVniEncapBUMBytes=_AristaVxlanVniEncapBUMBytes_Object((1,3,6,1,4,1,30065,3,28,1,2,1,12),_AristaVxlanVniEncapBUMBytes_Type())
aristaVxlanVniEncapBUMBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVniEncapBUMBytes.setStatus(_A)
_AristaVxlanVniEncapBUMPkts_Type=Counter64
_AristaVxlanVniEncapBUMPkts_Object=MibTableColumn
aristaVxlanVniEncapBUMPkts=_AristaVxlanVniEncapBUMPkts_Object((1,3,6,1,4,1,30065,3,28,1,2,1,13),_AristaVxlanVniEncapBUMPkts_Type())
aristaVxlanVniEncapBUMPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVniEncapBUMPkts.setStatus(_A)
_AristaVxlanVniEncapDropPkts_Type=Counter64
_AristaVxlanVniEncapDropPkts_Object=MibTableColumn
aristaVxlanVniEncapDropPkts=_AristaVxlanVniEncapDropPkts_Object((1,3,6,1,4,1,30065,3,28,1,2,1,14),_AristaVxlanVniEncapDropPkts_Type())
aristaVxlanVniEncapDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVniEncapDropPkts.setStatus(_A)
_AristaVxlanVtiVniCountersTable_Object=MibTable
aristaVxlanVtiVniCountersTable=_AristaVxlanVtiVniCountersTable_Object((1,3,6,1,4,1,30065,3,28,1,3))
if mibBuilder.loadTexts:aristaVxlanVtiVniCountersTable.setStatus(_A)
_AristaVxlanVtiVniCountersEntry_Object=MibTableRow
aristaVxlanVtiVniCountersEntry=_AristaVxlanVtiVniCountersEntry_Object((1,3,6,1,4,1,30065,3,28,1,3,1))
aristaVxlanVtiVniCountersEntry.setIndexNames((0,_B,_I),(0,_B,_E))
if mibBuilder.loadTexts:aristaVxlanVtiVniCountersEntry.setStatus(_A)
_AristaVxlanVtiIndex_Type=InterfaceIndex
_AristaVxlanVtiIndex_Object=MibTableColumn
aristaVxlanVtiIndex=_AristaVxlanVtiIndex_Object((1,3,6,1,4,1,30065,3,28,1,3,1,1),_AristaVxlanVtiIndex_Type())
aristaVxlanVtiIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaVxlanVtiIndex.setStatus(_A)
_AristaVxlanVtiVniDecapBytes_Type=Counter64
_AristaVxlanVtiVniDecapBytes_Object=MibTableColumn
aristaVxlanVtiVniDecapBytes=_AristaVxlanVtiVniDecapBytes_Object((1,3,6,1,4,1,30065,3,28,1,3,1,2),_AristaVxlanVtiVniDecapBytes_Type())
aristaVxlanVtiVniDecapBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVtiVniDecapBytes.setStatus(_A)
_AristaVxlanVtiVniDecapPkts_Type=Counter64
_AristaVxlanVtiVniDecapPkts_Object=MibTableColumn
aristaVxlanVtiVniDecapPkts=_AristaVxlanVtiVniDecapPkts_Object((1,3,6,1,4,1,30065,3,28,1,3,1,3),_AristaVxlanVtiVniDecapPkts_Type())
aristaVxlanVtiVniDecapPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVtiVniDecapPkts.setStatus(_A)
_AristaVxlanVtiVniEncapBytes_Type=Counter64
_AristaVxlanVtiVniEncapBytes_Object=MibTableColumn
aristaVxlanVtiVniEncapBytes=_AristaVxlanVtiVniEncapBytes_Object((1,3,6,1,4,1,30065,3,28,1,3,1,4),_AristaVxlanVtiVniEncapBytes_Type())
aristaVxlanVtiVniEncapBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVtiVniEncapBytes.setStatus(_A)
_AristaVxlanVtiVniEncapPkts_Type=Counter64
_AristaVxlanVtiVniEncapPkts_Object=MibTableColumn
aristaVxlanVtiVniEncapPkts=_AristaVxlanVtiVniEncapPkts_Object((1,3,6,1,4,1,30065,3,28,1,3,1,5),_AristaVxlanVtiVniEncapPkts_Type())
aristaVxlanVtiVniEncapPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVxlanVtiVniEncapPkts.setStatus(_A)
_AristaVxlanMibConformance_ObjectIdentity=ObjectIdentity
aristaVxlanMibConformance=_AristaVxlanMibConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,28,2))
_AristaVxlanMibCompliances_ObjectIdentity=ObjectIdentity
aristaVxlanMibCompliances=_AristaVxlanMibCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,28,2,1))
_AristaVxlanMibGroups_ObjectIdentity=ObjectIdentity
aristaVxlanMibGroups=_AristaVxlanMibGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,28,2,2))
aristaVxlanMibCountersGroup=ObjectGroup((1,3,6,1,4,1,30065,3,28,2,2,1))
aristaVxlanMibCountersGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:aristaVxlanMibCountersGroup.setStatus(_A)
aristaVxlanMibCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,28,2,1,1))
aristaVxlanMibCompliance.setObjects((_B,_m))
if mibBuilder.loadTexts:aristaVxlanMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'aristaVxlanMIB':aristaVxlanMIB,'aristaVxlanMibNotifications':aristaVxlanMibNotifications,'aristaVxlanMibObjects':aristaVxlanMibObjects,'aristaVxlanVtepCountersTable':aristaVxlanVtepCountersTable,'aristaVxlanVtepCountersEntry':aristaVxlanVtepCountersEntry,_G:aristaVxlanVtepAddressType,_H:aristaVxlanVtepAddress,_J:aristaVxlanVtepDecapBytes,_K:aristaVxlanVtepDecapPkts,_L:aristaVxlanVtepDecapKnownUcastBytes,_M:aristaVxlanVtepDecapKnownUcastPkts,_N:aristaVxlanVtepDecapBUMBytes,_O:aristaVxlanVtepDecapBUMPkts,_P:aristaVxlanVtepDecapDropExcptBytes,_Q:aristaVxlanVtepDecapDropExcptPkts,_R:aristaVxlanVtepEncapBytes,_S:aristaVxlanVtepEncapPkts,_T:aristaVxlanVtepEncapBUMPkts,_U:aristaVxlanVtepEncapDropExcptPkts,'aristaVxlanVniCountersTable':aristaVxlanVniCountersTable,'aristaVxlanVniCountersEntry':aristaVxlanVniCountersEntry,_E:aristaVxlanVni,_V:aristaVxlanVniDecapBytes,_W:aristaVxlanVniDecapPkts,_X:aristaVxlanVniDecapKnownUcastBytes,_Y:aristaVxlanVniDecapKnownUcastPkts,_Z:aristaVxlanVniDecapBUMBytes,_a:aristaVxlanVniDecapBUMPkts,_b:aristaVxlanVniDecapDropExcptBytes,_c:aristaVxlanVniDecapDropExcptPkts,_d:aristaVxlanVniEncapBytes,_e:aristaVxlanVniEncapPkts,_f:aristaVxlanVniEncapBUMBytes,_g:aristaVxlanVniEncapBUMPkts,_h:aristaVxlanVniEncapDropPkts,'aristaVxlanVtiVniCountersTable':aristaVxlanVtiVniCountersTable,'aristaVxlanVtiVniCountersEntry':aristaVxlanVtiVniCountersEntry,_I:aristaVxlanVtiIndex,_i:aristaVxlanVtiVniDecapBytes,_j:aristaVxlanVtiVniDecapPkts,_k:aristaVxlanVtiVniEncapBytes,_l:aristaVxlanVtiVniEncapPkts,'aristaVxlanMibConformance':aristaVxlanMibConformance,'aristaVxlanMibCompliances':aristaVxlanMibCompliances,'aristaVxlanMibCompliance':aristaVxlanMibCompliance,'aristaVxlanMibGroups':aristaVxlanMibGroups,_m:aristaVxlanMibCountersGroup})