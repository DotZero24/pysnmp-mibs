_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
local,=mibBuilder.importSymbols('CISCO-SMI','local')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Lcpu_ObjectIdentity=ObjectIdentity
lcpu=_Lcpu_ObjectIdentity((1,3,6,1,4,1,9,2,1))
_BusyPer_Type=Integer32
_BusyPer_Object=MibScalar
busyPer=_BusyPer_Object((1,3,6,1,4,1,9,2,1,56),_BusyPer_Type())
busyPer.setMaxAccess(_B)
if mibBuilder.loadTexts:busyPer.setStatus(_A)
_AvgBusy1_Type=Integer32
_AvgBusy1_Object=MibScalar
avgBusy1=_AvgBusy1_Object((1,3,6,1,4,1,9,2,1,57),_AvgBusy1_Type())
avgBusy1.setMaxAccess(_B)
if mibBuilder.loadTexts:avgBusy1.setStatus(_A)
_AvgBusy5_Type=Integer32
_AvgBusy5_Object=MibScalar
avgBusy5=_AvgBusy5_Object((1,3,6,1,4,1,9,2,1,58),_AvgBusy5_Type())
avgBusy5.setMaxAccess(_B)
if mibBuilder.loadTexts:avgBusy5.setStatus(_A)
_IdleCount_Type=Integer32
_IdleCount_Object=MibScalar
idleCount=_IdleCount_Object((1,3,6,1,4,1,9,2,1,59),_IdleCount_Type())
idleCount.setMaxAccess(_C)
if mibBuilder.loadTexts:idleCount.setStatus(_A)
_IdleWired_Type=Integer32
_IdleWired_Object=MibScalar
idleWired=_IdleWired_Object((1,3,6,1,4,1,9,2,1,60),_IdleWired_Type())
idleWired.setMaxAccess(_C)
if mibBuilder.loadTexts:idleWired.setStatus(_A)
mibBuilder.exportSymbols('OLD-CISCO-CPU-MIB',**{'lcpu':lcpu,'busyPer':busyPer,'avgBusy1':avgBusy1,'avgBusy5':avgBusy5,'idleCount':idleCount,'idleWired':idleWired})