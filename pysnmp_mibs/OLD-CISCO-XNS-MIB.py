_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
temporary,=mibBuilder.importSymbols('CISCO-SMI','temporary')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Tmpxns_ObjectIdentity=ObjectIdentity
tmpxns=_Tmpxns_ObjectIdentity((1,3,6,1,4,1,9,3,2))
_XnsInput_Type=Integer32
_XnsInput_Object=MibScalar
xnsInput=_XnsInput_Object((1,3,6,1,4,1,9,3,2,1),_XnsInput_Type())
xnsInput.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsInput.setStatus(_B)
_XnsLocal_Type=Integer32
_XnsLocal_Object=MibScalar
xnsLocal=_XnsLocal_Object((1,3,6,1,4,1,9,3,2,2),_XnsLocal_Type())
xnsLocal.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsLocal.setStatus(_B)
_XnsBcastin_Type=Integer32
_XnsBcastin_Object=MibScalar
xnsBcastin=_XnsBcastin_Object((1,3,6,1,4,1,9,3,2,3),_XnsBcastin_Type())
xnsBcastin.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsBcastin.setStatus(_B)
_XnsForward_Type=Integer32
_XnsForward_Object=MibScalar
xnsForward=_XnsForward_Object((1,3,6,1,4,1,9,3,2,4),_XnsForward_Type())
xnsForward.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsForward.setStatus(_B)
_XnsBcastout_Type=Integer32
_XnsBcastout_Object=MibScalar
xnsBcastout=_XnsBcastout_Object((1,3,6,1,4,1,9,3,2,5),_XnsBcastout_Type())
xnsBcastout.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsBcastout.setStatus(_B)
_XnsErrin_Type=Integer32
_XnsErrin_Object=MibScalar
xnsErrin=_XnsErrin_Object((1,3,6,1,4,1,9,3,2,6),_XnsErrin_Type())
xnsErrin.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsErrin.setStatus(_B)
_XnsErrout_Type=Integer32
_XnsErrout_Object=MibScalar
xnsErrout=_XnsErrout_Object((1,3,6,1,4,1,9,3,2,7),_XnsErrout_Type())
xnsErrout.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsErrout.setStatus(_B)
_XnsFormerr_Type=Integer32
_XnsFormerr_Object=MibScalar
xnsFormerr=_XnsFormerr_Object((1,3,6,1,4,1,9,3,2,8),_XnsFormerr_Type())
xnsFormerr.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsFormerr.setStatus(_B)
_XnsChksum_Type=Integer32
_XnsChksum_Object=MibScalar
xnsChksum=_XnsChksum_Object((1,3,6,1,4,1,9,3,2,9),_XnsChksum_Type())
xnsChksum.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsChksum.setStatus(_B)
_XnsNotgate_Type=Integer32
_XnsNotgate_Object=MibScalar
xnsNotgate=_XnsNotgate_Object((1,3,6,1,4,1,9,3,2,10),_XnsNotgate_Type())
xnsNotgate.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsNotgate.setStatus(_B)
_XnsHopcnt_Type=Integer32
_XnsHopcnt_Object=MibScalar
xnsHopcnt=_XnsHopcnt_Object((1,3,6,1,4,1,9,3,2,11),_XnsHopcnt_Type())
xnsHopcnt.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsHopcnt.setStatus(_B)
_XnsNoroute_Type=Integer32
_XnsNoroute_Object=MibScalar
xnsNoroute=_XnsNoroute_Object((1,3,6,1,4,1,9,3,2,12),_XnsNoroute_Type())
xnsNoroute.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsNoroute.setStatus(_B)
_XnsNoencap_Type=Integer32
_XnsNoencap_Object=MibScalar
xnsNoencap=_XnsNoencap_Object((1,3,6,1,4,1,9,3,2,13),_XnsNoencap_Type())
xnsNoencap.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsNoencap.setStatus(_B)
_XnsOutput_Type=Integer32
_XnsOutput_Object=MibScalar
xnsOutput=_XnsOutput_Object((1,3,6,1,4,1,9,3,2,14),_XnsOutput_Type())
xnsOutput.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsOutput.setStatus(_B)
_XnsInmult_Type=Integer32
_XnsInmult_Object=MibScalar
xnsInmult=_XnsInmult_Object((1,3,6,1,4,1,9,3,2,15),_XnsInmult_Type())
xnsInmult.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsInmult.setStatus(_B)
_XnsUnknown_Type=Integer32
_XnsUnknown_Object=MibScalar
xnsUnknown=_XnsUnknown_Object((1,3,6,1,4,1,9,3,2,16),_XnsUnknown_Type())
xnsUnknown.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsUnknown.setStatus(_B)
_XnsFwdbrd_Type=Integer32
_XnsFwdbrd_Object=MibScalar
xnsFwdbrd=_XnsFwdbrd_Object((1,3,6,1,4,1,9,3,2,17),_XnsFwdbrd_Type())
xnsFwdbrd.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsFwdbrd.setStatus(_B)
_XnsEchoreqin_Type=Integer32
_XnsEchoreqin_Object=MibScalar
xnsEchoreqin=_XnsEchoreqin_Object((1,3,6,1,4,1,9,3,2,18),_XnsEchoreqin_Type())
xnsEchoreqin.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsEchoreqin.setStatus(_B)
_XnsEchoreqout_Type=Integer32
_XnsEchoreqout_Object=MibScalar
xnsEchoreqout=_XnsEchoreqout_Object((1,3,6,1,4,1,9,3,2,19),_XnsEchoreqout_Type())
xnsEchoreqout.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsEchoreqout.setStatus(_B)
_XnsEchorepin_Type=Integer32
_XnsEchorepin_Object=MibScalar
xnsEchorepin=_XnsEchorepin_Object((1,3,6,1,4,1,9,3,2,20),_XnsEchorepin_Type())
xnsEchorepin.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsEchorepin.setStatus(_B)
_XnsEchorepout_Type=Integer32
_XnsEchorepout_Object=MibScalar
xnsEchorepout=_XnsEchorepout_Object((1,3,6,1,4,1,9,3,2,21),_XnsEchorepout_Type())
xnsEchorepout.setMaxAccess(_A)
if mibBuilder.loadTexts:xnsEchorepout.setStatus(_B)
mibBuilder.exportSymbols('OLD-CISCO-XNS-MIB',**{'tmpxns':tmpxns,'xnsInput':xnsInput,'xnsLocal':xnsLocal,'xnsBcastin':xnsBcastin,'xnsForward':xnsForward,'xnsBcastout':xnsBcastout,'xnsErrin':xnsErrin,'xnsErrout':xnsErrout,'xnsFormerr':xnsFormerr,'xnsChksum':xnsChksum,'xnsNotgate':xnsNotgate,'xnsHopcnt':xnsHopcnt,'xnsNoroute':xnsNoroute,'xnsNoencap':xnsNoencap,'xnsOutput':xnsOutput,'xnsInmult':xnsInmult,'xnsUnknown':xnsUnknown,'xnsFwdbrd':xnsFwdbrd,'xnsEchoreqin':xnsEchoreqin,'xnsEchoreqout':xnsEchoreqout,'xnsEchorepin':xnsEchorepin,'xnsEchorepout':xnsEchorepout})