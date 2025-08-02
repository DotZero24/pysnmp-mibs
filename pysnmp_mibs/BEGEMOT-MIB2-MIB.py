_D='read-write'
_C='read-only'
_B='TimeTicks'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
begemotIp,=mibBuilder.importSymbols('BEGEMOT-IP-MIB','begemotIp')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_B,'Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
begemotMib2=ModuleIdentity((1,3,6,1,4,1,12325,1,3,1))
if mibBuilder.loadTexts:begemotMib2.setRevisions(('2009-08-03 00:00','2006-02-13 00:00'))
_BegemotIfMaxspeed_Type=Counter64
_BegemotIfMaxspeed_Object=MibScalar
begemotIfMaxspeed=_BegemotIfMaxspeed_Object((1,3,6,1,4,1,12325,1,3,1,1),_BegemotIfMaxspeed_Type())
begemotIfMaxspeed.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotIfMaxspeed.setStatus(_A)
if mibBuilder.loadTexts:begemotIfMaxspeed.setUnits('bps')
_BegemotIfPoll_Type=TimeTicks
_BegemotIfPoll_Object=MibScalar
begemotIfPoll=_BegemotIfPoll_Object((1,3,6,1,4,1,12325,1,3,1,2),_BegemotIfPoll_Type())
begemotIfPoll.setMaxAccess(_C)
if mibBuilder.loadTexts:begemotIfPoll.setStatus(_A)
_BegemotIfForcePoll_Type=TimeTicks
_BegemotIfForcePoll_Object=MibScalar
begemotIfForcePoll=_BegemotIfForcePoll_Object((1,3,6,1,4,1,12325,1,3,1,3),_BegemotIfForcePoll_Type())
begemotIfForcePoll.setMaxAccess(_D)
if mibBuilder.loadTexts:begemotIfForcePoll.setStatus(_A)
class _BegemotIfDataPoll_Type(TimeTicks):defaultValue=100
_BegemotIfDataPoll_Type.__name__=_B
_BegemotIfDataPoll_Object=MibScalar
begemotIfDataPoll=_BegemotIfDataPoll_Object((1,3,6,1,4,1,12325,1,3,1,4),_BegemotIfDataPoll_Type())
begemotIfDataPoll.setMaxAccess(_D)
if mibBuilder.loadTexts:begemotIfDataPoll.setStatus(_A)
if mibBuilder.loadTexts:begemotIfDataPoll.setUnits('deciseconds')
mibBuilder.exportSymbols('BEGEMOT-MIB2-MIB',**{'begemotMib2':begemotMib2,'begemotIfMaxspeed':begemotIfMaxspeed,'begemotIfPoll':begemotIfPoll,'begemotIfForcePoll':begemotIfForcePoll,'begemotIfDataPoll':begemotIfDataPoll})