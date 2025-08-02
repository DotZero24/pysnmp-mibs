_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Biboip_ObjectIdentity=ObjectIdentity
biboip=_Biboip_ObjectIdentity((1,3,6,1,4,1,272,4,5))
_OspfStat_ObjectIdentity=ObjectIdentity
ospfStat=_OspfStat_ObjectIdentity((1,3,6,1,4,1,272,4,5,10))
_OspfStatHelloRecv_Type=Counter32
_OspfStatHelloRecv_Object=MibScalar
ospfStatHelloRecv=_OspfStatHelloRecv_Object((1,3,6,1,4,1,272,4,5,10,1),_OspfStatHelloRecv_Type())
ospfStatHelloRecv.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfStatHelloRecv.setStatus(_B)
_OspfStatHelloSent_Type=Counter32
_OspfStatHelloSent_Object=MibScalar
ospfStatHelloSent=_OspfStatHelloSent_Object((1,3,6,1,4,1,272,4,5,10,2),_OspfStatHelloSent_Type())
ospfStatHelloSent.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfStatHelloSent.setStatus(_B)
_OspfStatDdRecv_Type=Counter32
_OspfStatDdRecv_Object=MibScalar
ospfStatDdRecv=_OspfStatDdRecv_Object((1,3,6,1,4,1,272,4,5,10,3),_OspfStatDdRecv_Type())
ospfStatDdRecv.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfStatDdRecv.setStatus(_B)
_OspfStatDdSent_Type=Counter32
_OspfStatDdSent_Object=MibScalar
ospfStatDdSent=_OspfStatDdSent_Object((1,3,6,1,4,1,272,4,5,10,4),_OspfStatDdSent_Type())
ospfStatDdSent.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfStatDdSent.setStatus(_B)
_OspfStatLsackRecv_Type=Counter32
_OspfStatLsackRecv_Object=MibScalar
ospfStatLsackRecv=_OspfStatLsackRecv_Object((1,3,6,1,4,1,272,4,5,10,5),_OspfStatLsackRecv_Type())
ospfStatLsackRecv.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfStatLsackRecv.setStatus(_B)
_OspfStatLsackSent_Type=Counter32
_OspfStatLsackSent_Object=MibScalar
ospfStatLsackSent=_OspfStatLsackSent_Object((1,3,6,1,4,1,272,4,5,10,6),_OspfStatLsackSent_Type())
ospfStatLsackSent.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfStatLsackSent.setStatus(_B)
_OspfStatLsreqRecv_Type=Counter32
_OspfStatLsreqRecv_Object=MibScalar
ospfStatLsreqRecv=_OspfStatLsreqRecv_Object((1,3,6,1,4,1,272,4,5,10,7),_OspfStatLsreqRecv_Type())
ospfStatLsreqRecv.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfStatLsreqRecv.setStatus(_B)
_OspfStatLsreqSent_Type=Counter32
_OspfStatLsreqSent_Object=MibScalar
ospfStatLsreqSent=_OspfStatLsreqSent_Object((1,3,6,1,4,1,272,4,5,10,8),_OspfStatLsreqSent_Type())
ospfStatLsreqSent.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfStatLsreqSent.setStatus(_B)
_OspfStatLsupdRecv_Type=Counter32
_OspfStatLsupdRecv_Object=MibScalar
ospfStatLsupdRecv=_OspfStatLsupdRecv_Object((1,3,6,1,4,1,272,4,5,10,9),_OspfStatLsupdRecv_Type())
ospfStatLsupdRecv.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfStatLsupdRecv.setStatus(_B)
_OspfStatLsupdSent_Type=Counter32
_OspfStatLsupdSent_Object=MibScalar
ospfStatLsupdSent=_OspfStatLsupdSent_Object((1,3,6,1,4,1,272,4,5,10,10),_OspfStatLsupdSent_Type())
ospfStatLsupdSent.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfStatLsupdSent.setStatus(_B)
_OspfStatSummaryIncUpd_Type=Counter32
_OspfStatSummaryIncUpd_Object=MibScalar
ospfStatSummaryIncUpd=_OspfStatSummaryIncUpd_Object((1,3,6,1,4,1,272,4,5,10,11),_OspfStatSummaryIncUpd_Type())
ospfStatSummaryIncUpd.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfStatSummaryIncUpd.setStatus(_B)
_OspfStatExternalIncUpd_Type=Counter32
_OspfStatExternalIncUpd_Object=MibScalar
ospfStatExternalIncUpd=_OspfStatExternalIncUpd_Object((1,3,6,1,4,1,272,4,5,10,12),_OspfStatExternalIncUpd_Type())
ospfStatExternalIncUpd.setMaxAccess(_A)
if mibBuilder.loadTexts:ospfStatExternalIncUpd.setStatus(_B)
mibBuilder.exportSymbols('BIANCA-BRICK-OSPF-STAT-MIB',**{'bintec':bintec,'bibo':bibo,'biboip':biboip,'ospfStat':ospfStat,'ospfStatHelloRecv':ospfStatHelloRecv,'ospfStatHelloSent':ospfStatHelloSent,'ospfStatDdRecv':ospfStatDdRecv,'ospfStatDdSent':ospfStatDdSent,'ospfStatLsackRecv':ospfStatLsackRecv,'ospfStatLsackSent':ospfStatLsackSent,'ospfStatLsreqRecv':ospfStatLsreqRecv,'ospfStatLsreqSent':ospfStatLsreqSent,'ospfStatLsupdRecv':ospfStatLsupdRecv,'ospfStatLsupdSent':ospfStatLsupdSent,'ospfStatSummaryIncUpd':ospfStatSummaryIncUpd,'ospfStatExternalIncUpd':ospfStatExternalIncUpd})