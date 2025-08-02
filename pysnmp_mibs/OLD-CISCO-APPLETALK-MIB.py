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
_Tmpappletalk_ObjectIdentity=ObjectIdentity
tmpappletalk=_Tmpappletalk_ObjectIdentity((1,3,6,1,4,1,9,3,3))
_AtInput_Type=Integer32
_AtInput_Object=MibScalar
atInput=_AtInput_Object((1,3,6,1,4,1,9,3,3,1),_AtInput_Type())
atInput.setMaxAccess(_A)
if mibBuilder.loadTexts:atInput.setStatus(_B)
_AtLocal_Type=Integer32
_AtLocal_Object=MibScalar
atLocal=_AtLocal_Object((1,3,6,1,4,1,9,3,3,2),_AtLocal_Type())
atLocal.setMaxAccess(_A)
if mibBuilder.loadTexts:atLocal.setStatus(_B)
_AtBcastin_Type=Integer32
_AtBcastin_Object=MibScalar
atBcastin=_AtBcastin_Object((1,3,6,1,4,1,9,3,3,3),_AtBcastin_Type())
atBcastin.setMaxAccess(_A)
if mibBuilder.loadTexts:atBcastin.setStatus(_B)
_AtForward_Type=Integer32
_AtForward_Object=MibScalar
atForward=_AtForward_Object((1,3,6,1,4,1,9,3,3,4),_AtForward_Type())
atForward.setMaxAccess(_A)
if mibBuilder.loadTexts:atForward.setStatus(_B)
_AtBcastout_Type=Integer32
_AtBcastout_Object=MibScalar
atBcastout=_AtBcastout_Object((1,3,6,1,4,1,9,3,3,5),_AtBcastout_Type())
atBcastout.setMaxAccess(_A)
if mibBuilder.loadTexts:atBcastout.setStatus(_B)
_AtChksum_Type=Integer32
_AtChksum_Object=MibScalar
atChksum=_AtChksum_Object((1,3,6,1,4,1,9,3,3,7),_AtChksum_Type())
atChksum.setMaxAccess(_A)
if mibBuilder.loadTexts:atChksum.setStatus(_B)
_AtNotgate_Type=Integer32
_AtNotgate_Object=MibScalar
atNotgate=_AtNotgate_Object((1,3,6,1,4,1,9,3,3,8),_AtNotgate_Type())
atNotgate.setMaxAccess(_A)
if mibBuilder.loadTexts:atNotgate.setStatus(_B)
_AtHopcnt_Type=Integer32
_AtHopcnt_Object=MibScalar
atHopcnt=_AtHopcnt_Object((1,3,6,1,4,1,9,3,3,9),_AtHopcnt_Type())
atHopcnt.setMaxAccess(_A)
if mibBuilder.loadTexts:atHopcnt.setStatus(_B)
_AtNoaccess_Type=Integer32
_AtNoaccess_Object=MibScalar
atNoaccess=_AtNoaccess_Object((1,3,6,1,4,1,9,3,3,10),_AtNoaccess_Type())
atNoaccess.setMaxAccess(_A)
if mibBuilder.loadTexts:atNoaccess.setStatus(_B)
_AtNoroute_Type=Integer32
_AtNoroute_Object=MibScalar
atNoroute=_AtNoroute_Object((1,3,6,1,4,1,9,3,3,11),_AtNoroute_Type())
atNoroute.setMaxAccess(_A)
if mibBuilder.loadTexts:atNoroute.setStatus(_B)
_AtNoencap_Type=Integer32
_AtNoencap_Object=MibScalar
atNoencap=_AtNoencap_Object((1,3,6,1,4,1,9,3,3,12),_AtNoencap_Type())
atNoencap.setMaxAccess(_A)
if mibBuilder.loadTexts:atNoencap.setStatus(_B)
_AtOutput_Type=Integer32
_AtOutput_Object=MibScalar
atOutput=_AtOutput_Object((1,3,6,1,4,1,9,3,3,13),_AtOutput_Type())
atOutput.setMaxAccess(_A)
if mibBuilder.loadTexts:atOutput.setStatus(_B)
_AtInmult_Type=Integer32
_AtInmult_Object=MibScalar
atInmult=_AtInmult_Object((1,3,6,1,4,1,9,3,3,14),_AtInmult_Type())
atInmult.setMaxAccess(_A)
if mibBuilder.loadTexts:atInmult.setStatus(_B)
_AtRtmpin_Type=Integer32
_AtRtmpin_Object=MibScalar
atRtmpin=_AtRtmpin_Object((1,3,6,1,4,1,9,3,3,15),_AtRtmpin_Type())
atRtmpin.setMaxAccess(_A)
if mibBuilder.loadTexts:atRtmpin.setStatus(_B)
_AtRtmpout_Type=Integer32
_AtRtmpout_Object=MibScalar
atRtmpout=_AtRtmpout_Object((1,3,6,1,4,1,9,3,3,16),_AtRtmpout_Type())
atRtmpout.setMaxAccess(_A)
if mibBuilder.loadTexts:atRtmpout.setStatus(_B)
_AtNbpin_Type=Integer32
_AtNbpin_Object=MibScalar
atNbpin=_AtNbpin_Object((1,3,6,1,4,1,9,3,3,17),_AtNbpin_Type())
atNbpin.setMaxAccess(_A)
if mibBuilder.loadTexts:atNbpin.setStatus(_B)
_AtNbpout_Type=Integer32
_AtNbpout_Object=MibScalar
atNbpout=_AtNbpout_Object((1,3,6,1,4,1,9,3,3,18),_AtNbpout_Type())
atNbpout.setMaxAccess(_A)
if mibBuilder.loadTexts:atNbpout.setStatus(_B)
_AtAtp_Type=Integer32
_AtAtp_Object=MibScalar
atAtp=_AtAtp_Object((1,3,6,1,4,1,9,3,3,19),_AtAtp_Type())
atAtp.setMaxAccess(_A)
if mibBuilder.loadTexts:atAtp.setStatus(_B)
_AtZipin_Type=Integer32
_AtZipin_Object=MibScalar
atZipin=_AtZipin_Object((1,3,6,1,4,1,9,3,3,20),_AtZipin_Type())
atZipin.setMaxAccess(_A)
if mibBuilder.loadTexts:atZipin.setStatus(_B)
_AtZipout_Type=Integer32
_AtZipout_Object=MibScalar
atZipout=_AtZipout_Object((1,3,6,1,4,1,9,3,3,21),_AtZipout_Type())
atZipout.setMaxAccess(_A)
if mibBuilder.loadTexts:atZipout.setStatus(_B)
_AtEcho_Type=Integer32
_AtEcho_Object=MibScalar
atEcho=_AtEcho_Object((1,3,6,1,4,1,9,3,3,22),_AtEcho_Type())
atEcho.setMaxAccess(_A)
if mibBuilder.loadTexts:atEcho.setStatus(_B)
_AtEchoill_Type=Integer32
_AtEchoill_Object=MibScalar
atEchoill=_AtEchoill_Object((1,3,6,1,4,1,9,3,3,23),_AtEchoill_Type())
atEchoill.setMaxAccess(_A)
if mibBuilder.loadTexts:atEchoill.setStatus(_B)
_AtDdpshort_Type=Integer32
_AtDdpshort_Object=MibScalar
atDdpshort=_AtDdpshort_Object((1,3,6,1,4,1,9,3,3,24),_AtDdpshort_Type())
atDdpshort.setMaxAccess(_A)
if mibBuilder.loadTexts:atDdpshort.setStatus(_B)
_AtDdplong_Type=Integer32
_AtDdplong_Object=MibScalar
atDdplong=_AtDdplong_Object((1,3,6,1,4,1,9,3,3,25),_AtDdplong_Type())
atDdplong.setMaxAccess(_A)
if mibBuilder.loadTexts:atDdplong.setStatus(_B)
_AtDdpbad_Type=Integer32
_AtDdpbad_Object=MibScalar
atDdpbad=_AtDdpbad_Object((1,3,6,1,4,1,9,3,3,26),_AtDdpbad_Type())
atDdpbad.setMaxAccess(_A)
if mibBuilder.loadTexts:atDdpbad.setStatus(_B)
_AtNobuffer_Type=Integer32
_AtNobuffer_Object=MibScalar
atNobuffer=_AtNobuffer_Object((1,3,6,1,4,1,9,3,3,27),_AtNobuffer_Type())
atNobuffer.setMaxAccess(_A)
if mibBuilder.loadTexts:atNobuffer.setStatus(_B)
_AtArpreq_Type=Integer32
_AtArpreq_Object=MibScalar
atArpreq=_AtArpreq_Object((1,3,6,1,4,1,9,3,3,28),_AtArpreq_Type())
atArpreq.setMaxAccess(_A)
if mibBuilder.loadTexts:atArpreq.setStatus(_B)
_AtArpreply_Type=Integer32
_AtArpreply_Object=MibScalar
atArpreply=_AtArpreply_Object((1,3,6,1,4,1,9,3,3,29),_AtArpreply_Type())
atArpreply.setMaxAccess(_A)
if mibBuilder.loadTexts:atArpreply.setStatus(_B)
_AtArpprobe_Type=Integer32
_AtArpprobe_Object=MibScalar
atArpprobe=_AtArpprobe_Object((1,3,6,1,4,1,9,3,3,30),_AtArpprobe_Type())
atArpprobe.setMaxAccess(_A)
if mibBuilder.loadTexts:atArpprobe.setStatus(_B)
_AtUnknown_Type=Integer32
_AtUnknown_Object=MibScalar
atUnknown=_AtUnknown_Object((1,3,6,1,4,1,9,3,3,31),_AtUnknown_Type())
atUnknown.setMaxAccess(_A)
if mibBuilder.loadTexts:atUnknown.setStatus(_B)
mibBuilder.exportSymbols('OLD-CISCO-APPLETALK-MIB',**{'tmpappletalk':tmpappletalk,'atInput':atInput,'atLocal':atLocal,'atBcastin':atBcastin,'atForward':atForward,'atBcastout':atBcastout,'atChksum':atChksum,'atNotgate':atNotgate,'atHopcnt':atHopcnt,'atNoaccess':atNoaccess,'atNoroute':atNoroute,'atNoencap':atNoencap,'atOutput':atOutput,'atInmult':atInmult,'atRtmpin':atRtmpin,'atRtmpout':atRtmpout,'atNbpin':atNbpin,'atNbpout':atNbpout,'atAtp':atAtp,'atZipin':atZipin,'atZipout':atZipout,'atEcho':atEcho,'atEchoill':atEchoill,'atDdpshort':atDdpshort,'atDdplong':atDdplong,'atDdpbad':atDdpbad,'atNobuffer':atNobuffer,'atArpreq':atArpreq,'atArpreply':atArpreply,'atArpprobe':atArpprobe,'atUnknown':atUnknown})