_I='not-accessible'
_H='dnHIdx2'
_G='dnHIdx1'
_F='dnArea'
_E='ifIndex'
_D='IF-MIB'
_C='OLD-CISCO-DECNET-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
temporary,=mibBuilder.importSymbols('CISCO-SMI','temporary')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Tmpdecnet_ObjectIdentity=ObjectIdentity
tmpdecnet=_Tmpdecnet_ObjectIdentity((1,3,6,1,4,1,9,3,1))
_DnForward_Type=Integer32
_DnForward_Object=MibScalar
dnForward=_DnForward_Object((1,3,6,1,4,1,9,3,1,1),_DnForward_Type())
dnForward.setMaxAccess(_B)
if mibBuilder.loadTexts:dnForward.setStatus(_A)
_DnReceived_Type=Integer32
_DnReceived_Object=MibScalar
dnReceived=_DnReceived_Object((1,3,6,1,4,1,9,3,1,2),_DnReceived_Type())
dnReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:dnReceived.setStatus(_A)
_DnFormaterr_Type=Integer32
_DnFormaterr_Object=MibScalar
dnFormaterr=_DnFormaterr_Object((1,3,6,1,4,1,9,3,1,3),_DnFormaterr_Type())
dnFormaterr.setMaxAccess(_B)
if mibBuilder.loadTexts:dnFormaterr.setStatus(_A)
_DnNotgateway_Type=Integer32
_DnNotgateway_Object=MibScalar
dnNotgateway=_DnNotgateway_Object((1,3,6,1,4,1,9,3,1,4),_DnNotgateway_Type())
dnNotgateway.setMaxAccess(_B)
if mibBuilder.loadTexts:dnNotgateway.setStatus(_A)
_DnNotimp_Type=Integer32
_DnNotimp_Object=MibScalar
dnNotimp=_DnNotimp_Object((1,3,6,1,4,1,9,3,1,5),_DnNotimp_Type())
dnNotimp.setMaxAccess(_B)
if mibBuilder.loadTexts:dnNotimp.setStatus(_A)
_DnHellos_Type=Integer32
_DnHellos_Object=MibScalar
dnHellos=_DnHellos_Object((1,3,6,1,4,1,9,3,1,6),_DnHellos_Type())
dnHellos.setMaxAccess(_B)
if mibBuilder.loadTexts:dnHellos.setStatus(_A)
_DnBadhello_Type=Integer32
_DnBadhello_Object=MibScalar
dnBadhello=_DnBadhello_Object((1,3,6,1,4,1,9,3,1,7),_DnBadhello_Type())
dnBadhello.setMaxAccess(_B)
if mibBuilder.loadTexts:dnBadhello.setStatus(_A)
_DnNotlong_Type=Integer32
_DnNotlong_Object=MibScalar
dnNotlong=_DnNotlong_Object((1,3,6,1,4,1,9,3,1,8),_DnNotlong_Type())
dnNotlong.setMaxAccess(_B)
if mibBuilder.loadTexts:dnNotlong.setStatus(_A)
_DnDatas_Type=Integer32
_DnDatas_Object=MibScalar
dnDatas=_DnDatas_Object((1,3,6,1,4,1,9,3,1,9),_DnDatas_Type())
dnDatas.setMaxAccess(_B)
if mibBuilder.loadTexts:dnDatas.setStatus(_A)
_DnBigaddr_Type=Integer32
_DnBigaddr_Object=MibScalar
dnBigaddr=_DnBigaddr_Object((1,3,6,1,4,1,9,3,1,10),_DnBigaddr_Type())
dnBigaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dnBigaddr.setStatus(_A)
_DnNoroute_Type=Integer32
_DnNoroute_Object=MibScalar
dnNoroute=_DnNoroute_Object((1,3,6,1,4,1,9,3,1,11),_DnNoroute_Type())
dnNoroute.setMaxAccess(_B)
if mibBuilder.loadTexts:dnNoroute.setStatus(_A)
_DnNoencap_Type=Integer32
_DnNoencap_Object=MibScalar
dnNoencap=_DnNoencap_Object((1,3,6,1,4,1,9,3,1,12),_DnNoencap_Type())
dnNoencap.setMaxAccess(_B)
if mibBuilder.loadTexts:dnNoencap.setStatus(_A)
_DnLevel1s_Type=Integer32
_DnLevel1s_Object=MibScalar
dnLevel1s=_DnLevel1s_Object((1,3,6,1,4,1,9,3,1,13),_DnLevel1s_Type())
dnLevel1s.setMaxAccess(_B)
if mibBuilder.loadTexts:dnLevel1s.setStatus(_A)
_DnBadlevel1_Type=Integer32
_DnBadlevel1_Object=MibScalar
dnBadlevel1=_DnBadlevel1_Object((1,3,6,1,4,1,9,3,1,14),_DnBadlevel1_Type())
dnBadlevel1.setMaxAccess(_B)
if mibBuilder.loadTexts:dnBadlevel1.setStatus(_A)
_DnToomanyhops_Type=Integer32
_DnToomanyhops_Object=MibScalar
dnToomanyhops=_DnToomanyhops_Object((1,3,6,1,4,1,9,3,1,15),_DnToomanyhops_Type())
dnToomanyhops.setMaxAccess(_B)
if mibBuilder.loadTexts:dnToomanyhops.setStatus(_A)
_DnHellosent_Type=Integer32
_DnHellosent_Object=MibScalar
dnHellosent=_DnHellosent_Object((1,3,6,1,4,1,9,3,1,16),_DnHellosent_Type())
dnHellosent.setMaxAccess(_B)
if mibBuilder.loadTexts:dnHellosent.setStatus(_A)
_DnLevel1sent_Type=Integer32
_DnLevel1sent_Object=MibScalar
dnLevel1sent=_DnLevel1sent_Object((1,3,6,1,4,1,9,3,1,17),_DnLevel1sent_Type())
dnLevel1sent.setMaxAccess(_B)
if mibBuilder.loadTexts:dnLevel1sent.setStatus(_A)
_DnNomemory_Type=Integer32
_DnNomemory_Object=MibScalar
dnNomemory=_DnNomemory_Object((1,3,6,1,4,1,9,3,1,18),_DnNomemory_Type())
dnNomemory.setMaxAccess(_B)
if mibBuilder.loadTexts:dnNomemory.setStatus(_A)
_DnOtherhello_Type=Integer32
_DnOtherhello_Object=MibScalar
dnOtherhello=_DnOtherhello_Object((1,3,6,1,4,1,9,3,1,19),_DnOtherhello_Type())
dnOtherhello.setMaxAccess(_B)
if mibBuilder.loadTexts:dnOtherhello.setStatus(_A)
_DnOtherlevel1_Type=Integer32
_DnOtherlevel1_Object=MibScalar
dnOtherlevel1=_DnOtherlevel1_Object((1,3,6,1,4,1,9,3,1,20),_DnOtherlevel1_Type())
dnOtherlevel1.setMaxAccess(_B)
if mibBuilder.loadTexts:dnOtherlevel1.setStatus(_A)
_DnLevel2s_Type=Integer32
_DnLevel2s_Object=MibScalar
dnLevel2s=_DnLevel2s_Object((1,3,6,1,4,1,9,3,1,21),_DnLevel2s_Type())
dnLevel2s.setMaxAccess(_B)
if mibBuilder.loadTexts:dnLevel2s.setStatus(_A)
_DnLevel2sent_Type=Integer32
_DnLevel2sent_Object=MibScalar
dnLevel2sent=_DnLevel2sent_Object((1,3,6,1,4,1,9,3,1,22),_DnLevel2sent_Type())
dnLevel2sent.setMaxAccess(_B)
if mibBuilder.loadTexts:dnLevel2sent.setStatus(_A)
_DnNovector_Type=Integer32
_DnNovector_Object=MibScalar
dnNovector=_DnNovector_Object((1,3,6,1,4,1,9,3,1,23),_DnNovector_Type())
dnNovector.setMaxAccess(_B)
if mibBuilder.loadTexts:dnNovector.setStatus(_A)
_DnOtherlevel2_Type=Integer32
_DnOtherlevel2_Object=MibScalar
dnOtherlevel2=_DnOtherlevel2_Object((1,3,6,1,4,1,9,3,1,24),_DnOtherlevel2_Type())
dnOtherlevel2.setMaxAccess(_B)
if mibBuilder.loadTexts:dnOtherlevel2.setStatus(_A)
_DnNoaccess_Type=Integer32
_DnNoaccess_Object=MibScalar
dnNoaccess=_DnNoaccess_Object((1,3,6,1,4,1,9,3,1,25),_DnNoaccess_Type())
dnNoaccess.setMaxAccess(_B)
if mibBuilder.loadTexts:dnNoaccess.setStatus(_A)
_DnAreaTable_Object=MibTable
dnAreaTable=_DnAreaTable_Object((1,3,6,1,4,1,9,3,1,26))
if mibBuilder.loadTexts:dnAreaTable.setStatus(_A)
_DnAreaTableEntry_Object=MibTableRow
dnAreaTableEntry=_DnAreaTableEntry_Object((1,3,6,1,4,1,9,3,1,26,1))
dnAreaTableEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:dnAreaTableEntry.setStatus(_A)
_DnArea_Type=Integer32
_DnArea_Object=MibTableColumn
dnArea=_DnArea_Object((1,3,6,1,4,1,9,3,1,26,1,1),_DnArea_Type())
dnArea.setMaxAccess(_B)
if mibBuilder.loadTexts:dnArea.setStatus(_A)
_DnACost_Type=Integer32
_DnACost_Object=MibTableColumn
dnACost=_DnACost_Object((1,3,6,1,4,1,9,3,1,26,1,2),_DnACost_Type())
dnACost.setMaxAccess(_B)
if mibBuilder.loadTexts:dnACost.setStatus(_A)
_DnAHop_Type=Integer32
_DnAHop_Object=MibTableColumn
dnAHop=_DnAHop_Object((1,3,6,1,4,1,9,3,1,26,1,3),_DnAHop_Type())
dnAHop.setMaxAccess(_B)
if mibBuilder.loadTexts:dnAHop.setStatus(_A)
_DnAIfIndex_Type=Integer32
_DnAIfIndex_Object=MibTableColumn
dnAIfIndex=_DnAIfIndex_Object((1,3,6,1,4,1,9,3,1,26,1,4),_DnAIfIndex_Type())
dnAIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dnAIfIndex.setStatus(_A)
_DnANextHop_Type=OctetString
_DnANextHop_Object=MibTableColumn
dnANextHop=_DnANextHop_Object((1,3,6,1,4,1,9,3,1,26,1,5),_DnANextHop_Type())
dnANextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:dnANextHop.setStatus(_A)
_DnAAge_Type=Integer32
_DnAAge_Object=MibTableColumn
dnAAge=_DnAAge_Object((1,3,6,1,4,1,9,3,1,26,1,6),_DnAAge_Type())
dnAAge.setMaxAccess(_B)
if mibBuilder.loadTexts:dnAAge.setStatus(_A)
_DnAPrio_Type=Integer32
_DnAPrio_Object=MibTableColumn
dnAPrio=_DnAPrio_Object((1,3,6,1,4,1,9,3,1,26,1,7),_DnAPrio_Type())
dnAPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:dnAPrio.setStatus(_A)
_DnHostTable_Object=MibTable
dnHostTable=_DnHostTable_Object((1,3,6,1,4,1,9,3,1,27))
if mibBuilder.loadTexts:dnHostTable.setStatus(_A)
_DnHostTableEntry_Object=MibTableRow
dnHostTableEntry=_DnHostTableEntry_Object((1,3,6,1,4,1,9,3,1,27,1))
dnHostTableEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:dnHostTableEntry.setStatus(_A)
_DnHost_Type=Integer32
_DnHost_Object=MibTableColumn
dnHost=_DnHost_Object((1,3,6,1,4,1,9,3,1,27,1,1),_DnHost_Type())
dnHost.setMaxAccess(_B)
if mibBuilder.loadTexts:dnHost.setStatus(_A)
_DnHCost_Type=Integer32
_DnHCost_Object=MibTableColumn
dnHCost=_DnHCost_Object((1,3,6,1,4,1,9,3,1,27,1,2),_DnHCost_Type())
dnHCost.setMaxAccess(_B)
if mibBuilder.loadTexts:dnHCost.setStatus(_A)
_DnHHop_Type=Integer32
_DnHHop_Object=MibTableColumn
dnHHop=_DnHHop_Object((1,3,6,1,4,1,9,3,1,27,1,3),_DnHHop_Type())
dnHHop.setMaxAccess(_B)
if mibBuilder.loadTexts:dnHHop.setStatus(_A)
_DnHIfIndex_Type=Integer32
_DnHIfIndex_Object=MibTableColumn
dnHIfIndex=_DnHIfIndex_Object((1,3,6,1,4,1,9,3,1,27,1,4),_DnHIfIndex_Type())
dnHIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dnHIfIndex.setStatus(_A)
_DnHNextHop_Type=OctetString
_DnHNextHop_Object=MibTableColumn
dnHNextHop=_DnHNextHop_Object((1,3,6,1,4,1,9,3,1,27,1,5),_DnHNextHop_Type())
dnHNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:dnHNextHop.setStatus(_A)
_DnHAge_Type=Integer32
_DnHAge_Object=MibTableColumn
dnHAge=_DnHAge_Object((1,3,6,1,4,1,9,3,1,27,1,6),_DnHAge_Type())
dnHAge.setMaxAccess(_B)
if mibBuilder.loadTexts:dnHAge.setStatus(_A)
_DnHPrio_Type=Integer32
_DnHPrio_Object=MibTableColumn
dnHPrio=_DnHPrio_Object((1,3,6,1,4,1,9,3,1,27,1,7),_DnHPrio_Type())
dnHPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:dnHPrio.setStatus(_A)
_DnHIdx1_Type=Integer32
_DnHIdx1_Object=MibTableColumn
dnHIdx1=_DnHIdx1_Object((1,3,6,1,4,1,9,3,1,27,1,8),_DnHIdx1_Type())
dnHIdx1.setMaxAccess(_I)
if mibBuilder.loadTexts:dnHIdx1.setStatus(_A)
_DnHIdx2_Type=Integer32
_DnHIdx2_Object=MibTableColumn
dnHIdx2=_DnHIdx2_Object((1,3,6,1,4,1,9,3,1,27,1,9),_DnHIdx2_Type())
dnHIdx2.setMaxAccess(_I)
if mibBuilder.loadTexts:dnHIdx2.setStatus(_A)
_DnIfTable_Object=MibTable
dnIfTable=_DnIfTable_Object((1,3,6,1,4,1,9,3,1,28))
if mibBuilder.loadTexts:dnIfTable.setStatus(_A)
_DnIfTableEntry_Object=MibTableRow
dnIfTableEntry=_DnIfTableEntry_Object((1,3,6,1,4,1,9,3,1,28,1))
dnIfTableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:dnIfTableEntry.setStatus(_A)
_DnIfCost_Type=Integer32
_DnIfCost_Object=MibTableColumn
dnIfCost=_DnIfCost_Object((1,3,6,1,4,1,9,3,1,28,1,1),_DnIfCost_Type())
dnIfCost.setMaxAccess(_B)
if mibBuilder.loadTexts:dnIfCost.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'tmpdecnet':tmpdecnet,'dnForward':dnForward,'dnReceived':dnReceived,'dnFormaterr':dnFormaterr,'dnNotgateway':dnNotgateway,'dnNotimp':dnNotimp,'dnHellos':dnHellos,'dnBadhello':dnBadhello,'dnNotlong':dnNotlong,'dnDatas':dnDatas,'dnBigaddr':dnBigaddr,'dnNoroute':dnNoroute,'dnNoencap':dnNoencap,'dnLevel1s':dnLevel1s,'dnBadlevel1':dnBadlevel1,'dnToomanyhops':dnToomanyhops,'dnHellosent':dnHellosent,'dnLevel1sent':dnLevel1sent,'dnNomemory':dnNomemory,'dnOtherhello':dnOtherhello,'dnOtherlevel1':dnOtherlevel1,'dnLevel2s':dnLevel2s,'dnLevel2sent':dnLevel2sent,'dnNovector':dnNovector,'dnOtherlevel2':dnOtherlevel2,'dnNoaccess':dnNoaccess,'dnAreaTable':dnAreaTable,'dnAreaTableEntry':dnAreaTableEntry,_F:dnArea,'dnACost':dnACost,'dnAHop':dnAHop,'dnAIfIndex':dnAIfIndex,'dnANextHop':dnANextHop,'dnAAge':dnAAge,'dnAPrio':dnAPrio,'dnHostTable':dnHostTable,'dnHostTableEntry':dnHostTableEntry,'dnHost':dnHost,'dnHCost':dnHCost,'dnHHop':dnHHop,'dnHIfIndex':dnHIfIndex,'dnHNextHop':dnHNextHop,'dnHAge':dnHAge,'dnHPrio':dnHPrio,_G:dnHIdx1,_H:dnHIdx2,'dnIfTable':dnIfTable,'dnIfTableEntry':dnIfTableEntry,'dnIfCost':dnIfCost})