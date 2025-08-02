_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
local,=mibBuilder.importSymbols('CISCO-SMI','local')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Lmem_ObjectIdentity=ObjectIdentity
lmem=_Lmem_ObjectIdentity((1,3,6,1,4,1,9,2,1))
_FreeMem_Type=Integer32
_FreeMem_Object=MibScalar
freeMem=_FreeMem_Object((1,3,6,1,4,1,9,2,1,8),_FreeMem_Type())
freeMem.setMaxAccess(_A)
if mibBuilder.loadTexts:freeMem.setStatus('obsolete')
_BufferElFree_Type=Integer32
_BufferElFree_Object=MibScalar
bufferElFree=_BufferElFree_Object((1,3,6,1,4,1,9,2,1,9),_BufferElFree_Type())
bufferElFree.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferElFree.setStatus(_B)
_BufferElMax_Type=Integer32
_BufferElMax_Object=MibScalar
bufferElMax=_BufferElMax_Object((1,3,6,1,4,1,9,2,1,10),_BufferElMax_Type())
bufferElMax.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferElMax.setStatus(_B)
_BufferElHit_Type=Integer32
_BufferElHit_Object=MibScalar
bufferElHit=_BufferElHit_Object((1,3,6,1,4,1,9,2,1,11),_BufferElHit_Type())
bufferElHit.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferElHit.setStatus(_B)
_BufferElMiss_Type=Integer32
_BufferElMiss_Object=MibScalar
bufferElMiss=_BufferElMiss_Object((1,3,6,1,4,1,9,2,1,12),_BufferElMiss_Type())
bufferElMiss.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferElMiss.setStatus(_B)
_BufferElCreate_Type=Integer32
_BufferElCreate_Object=MibScalar
bufferElCreate=_BufferElCreate_Object((1,3,6,1,4,1,9,2,1,13),_BufferElCreate_Type())
bufferElCreate.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferElCreate.setStatus(_B)
_BufferSmSize_Type=Integer32
_BufferSmSize_Object=MibScalar
bufferSmSize=_BufferSmSize_Object((1,3,6,1,4,1,9,2,1,14),_BufferSmSize_Type())
bufferSmSize.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferSmSize.setStatus(_B)
_BufferSmTotal_Type=Integer32
_BufferSmTotal_Object=MibScalar
bufferSmTotal=_BufferSmTotal_Object((1,3,6,1,4,1,9,2,1,15),_BufferSmTotal_Type())
bufferSmTotal.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferSmTotal.setStatus(_B)
_BufferSmFree_Type=Integer32
_BufferSmFree_Object=MibScalar
bufferSmFree=_BufferSmFree_Object((1,3,6,1,4,1,9,2,1,16),_BufferSmFree_Type())
bufferSmFree.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferSmFree.setStatus(_B)
_BufferSmMax_Type=Integer32
_BufferSmMax_Object=MibScalar
bufferSmMax=_BufferSmMax_Object((1,3,6,1,4,1,9,2,1,17),_BufferSmMax_Type())
bufferSmMax.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferSmMax.setStatus(_B)
_BufferSmHit_Type=Integer32
_BufferSmHit_Object=MibScalar
bufferSmHit=_BufferSmHit_Object((1,3,6,1,4,1,9,2,1,18),_BufferSmHit_Type())
bufferSmHit.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferSmHit.setStatus(_B)
_BufferSmMiss_Type=Integer32
_BufferSmMiss_Object=MibScalar
bufferSmMiss=_BufferSmMiss_Object((1,3,6,1,4,1,9,2,1,19),_BufferSmMiss_Type())
bufferSmMiss.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferSmMiss.setStatus(_B)
_BufferSmTrim_Type=Integer32
_BufferSmTrim_Object=MibScalar
bufferSmTrim=_BufferSmTrim_Object((1,3,6,1,4,1,9,2,1,20),_BufferSmTrim_Type())
bufferSmTrim.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferSmTrim.setStatus(_B)
_BufferSmCreate_Type=Integer32
_BufferSmCreate_Object=MibScalar
bufferSmCreate=_BufferSmCreate_Object((1,3,6,1,4,1,9,2,1,21),_BufferSmCreate_Type())
bufferSmCreate.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferSmCreate.setStatus(_B)
_BufferMdSize_Type=Integer32
_BufferMdSize_Object=MibScalar
bufferMdSize=_BufferMdSize_Object((1,3,6,1,4,1,9,2,1,22),_BufferMdSize_Type())
bufferMdSize.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferMdSize.setStatus(_B)
_BufferMdTotal_Type=Integer32
_BufferMdTotal_Object=MibScalar
bufferMdTotal=_BufferMdTotal_Object((1,3,6,1,4,1,9,2,1,23),_BufferMdTotal_Type())
bufferMdTotal.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferMdTotal.setStatus(_B)
_BufferMdFree_Type=Integer32
_BufferMdFree_Object=MibScalar
bufferMdFree=_BufferMdFree_Object((1,3,6,1,4,1,9,2,1,24),_BufferMdFree_Type())
bufferMdFree.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferMdFree.setStatus(_B)
_BufferMdMax_Type=Integer32
_BufferMdMax_Object=MibScalar
bufferMdMax=_BufferMdMax_Object((1,3,6,1,4,1,9,2,1,25),_BufferMdMax_Type())
bufferMdMax.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferMdMax.setStatus(_B)
_BufferMdHit_Type=Integer32
_BufferMdHit_Object=MibScalar
bufferMdHit=_BufferMdHit_Object((1,3,6,1,4,1,9,2,1,26),_BufferMdHit_Type())
bufferMdHit.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferMdHit.setStatus(_B)
_BufferMdMiss_Type=Integer32
_BufferMdMiss_Object=MibScalar
bufferMdMiss=_BufferMdMiss_Object((1,3,6,1,4,1,9,2,1,27),_BufferMdMiss_Type())
bufferMdMiss.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferMdMiss.setStatus(_B)
_BufferMdTrim_Type=Integer32
_BufferMdTrim_Object=MibScalar
bufferMdTrim=_BufferMdTrim_Object((1,3,6,1,4,1,9,2,1,28),_BufferMdTrim_Type())
bufferMdTrim.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferMdTrim.setStatus(_B)
_BufferMdCreate_Type=Integer32
_BufferMdCreate_Object=MibScalar
bufferMdCreate=_BufferMdCreate_Object((1,3,6,1,4,1,9,2,1,29),_BufferMdCreate_Type())
bufferMdCreate.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferMdCreate.setStatus(_B)
_BufferBgSize_Type=Integer32
_BufferBgSize_Object=MibScalar
bufferBgSize=_BufferBgSize_Object((1,3,6,1,4,1,9,2,1,30),_BufferBgSize_Type())
bufferBgSize.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferBgSize.setStatus(_B)
_BufferBgTotal_Type=Integer32
_BufferBgTotal_Object=MibScalar
bufferBgTotal=_BufferBgTotal_Object((1,3,6,1,4,1,9,2,1,31),_BufferBgTotal_Type())
bufferBgTotal.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferBgTotal.setStatus(_B)
_BufferBgFree_Type=Integer32
_BufferBgFree_Object=MibScalar
bufferBgFree=_BufferBgFree_Object((1,3,6,1,4,1,9,2,1,32),_BufferBgFree_Type())
bufferBgFree.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferBgFree.setStatus(_B)
_BufferBgMax_Type=Integer32
_BufferBgMax_Object=MibScalar
bufferBgMax=_BufferBgMax_Object((1,3,6,1,4,1,9,2,1,33),_BufferBgMax_Type())
bufferBgMax.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferBgMax.setStatus(_B)
_BufferBgHit_Type=Integer32
_BufferBgHit_Object=MibScalar
bufferBgHit=_BufferBgHit_Object((1,3,6,1,4,1,9,2,1,34),_BufferBgHit_Type())
bufferBgHit.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferBgHit.setStatus(_B)
_BufferBgMiss_Type=Integer32
_BufferBgMiss_Object=MibScalar
bufferBgMiss=_BufferBgMiss_Object((1,3,6,1,4,1,9,2,1,35),_BufferBgMiss_Type())
bufferBgMiss.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferBgMiss.setStatus(_B)
_BufferBgTrim_Type=Integer32
_BufferBgTrim_Object=MibScalar
bufferBgTrim=_BufferBgTrim_Object((1,3,6,1,4,1,9,2,1,36),_BufferBgTrim_Type())
bufferBgTrim.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferBgTrim.setStatus(_B)
_BufferBgCreate_Type=Integer32
_BufferBgCreate_Object=MibScalar
bufferBgCreate=_BufferBgCreate_Object((1,3,6,1,4,1,9,2,1,37),_BufferBgCreate_Type())
bufferBgCreate.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferBgCreate.setStatus(_B)
_BufferLgSize_Type=Integer32
_BufferLgSize_Object=MibScalar
bufferLgSize=_BufferLgSize_Object((1,3,6,1,4,1,9,2,1,38),_BufferLgSize_Type())
bufferLgSize.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferLgSize.setStatus(_B)
_BufferLgTotal_Type=Integer32
_BufferLgTotal_Object=MibScalar
bufferLgTotal=_BufferLgTotal_Object((1,3,6,1,4,1,9,2,1,39),_BufferLgTotal_Type())
bufferLgTotal.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferLgTotal.setStatus(_B)
_BufferLgFree_Type=Integer32
_BufferLgFree_Object=MibScalar
bufferLgFree=_BufferLgFree_Object((1,3,6,1,4,1,9,2,1,40),_BufferLgFree_Type())
bufferLgFree.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferLgFree.setStatus(_B)
_BufferLgMax_Type=Integer32
_BufferLgMax_Object=MibScalar
bufferLgMax=_BufferLgMax_Object((1,3,6,1,4,1,9,2,1,41),_BufferLgMax_Type())
bufferLgMax.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferLgMax.setStatus(_B)
_BufferLgHit_Type=Integer32
_BufferLgHit_Object=MibScalar
bufferLgHit=_BufferLgHit_Object((1,3,6,1,4,1,9,2,1,42),_BufferLgHit_Type())
bufferLgHit.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferLgHit.setStatus(_B)
_BufferLgMiss_Type=Integer32
_BufferLgMiss_Object=MibScalar
bufferLgMiss=_BufferLgMiss_Object((1,3,6,1,4,1,9,2,1,43),_BufferLgMiss_Type())
bufferLgMiss.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferLgMiss.setStatus(_B)
_BufferLgTrim_Type=Integer32
_BufferLgTrim_Object=MibScalar
bufferLgTrim=_BufferLgTrim_Object((1,3,6,1,4,1,9,2,1,44),_BufferLgTrim_Type())
bufferLgTrim.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferLgTrim.setStatus(_B)
_BufferLgCreate_Type=Integer32
_BufferLgCreate_Object=MibScalar
bufferLgCreate=_BufferLgCreate_Object((1,3,6,1,4,1,9,2,1,45),_BufferLgCreate_Type())
bufferLgCreate.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferLgCreate.setStatus(_B)
_BufferFail_Type=Integer32
_BufferFail_Object=MibScalar
bufferFail=_BufferFail_Object((1,3,6,1,4,1,9,2,1,46),_BufferFail_Type())
bufferFail.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferFail.setStatus(_B)
_BufferNoMem_Type=Integer32
_BufferNoMem_Object=MibScalar
bufferNoMem=_BufferNoMem_Object((1,3,6,1,4,1,9,2,1,47),_BufferNoMem_Type())
bufferNoMem.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferNoMem.setStatus(_B)
_BufferHgSize_Type=Integer32
_BufferHgSize_Object=MibScalar
bufferHgSize=_BufferHgSize_Object((1,3,6,1,4,1,9,2,1,62),_BufferHgSize_Type())
bufferHgSize.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferHgSize.setStatus(_B)
_BufferHgTotal_Type=Integer32
_BufferHgTotal_Object=MibScalar
bufferHgTotal=_BufferHgTotal_Object((1,3,6,1,4,1,9,2,1,63),_BufferHgTotal_Type())
bufferHgTotal.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferHgTotal.setStatus(_B)
_BufferHgFree_Type=Integer32
_BufferHgFree_Object=MibScalar
bufferHgFree=_BufferHgFree_Object((1,3,6,1,4,1,9,2,1,64),_BufferHgFree_Type())
bufferHgFree.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferHgFree.setStatus(_B)
_BufferHgMax_Type=Integer32
_BufferHgMax_Object=MibScalar
bufferHgMax=_BufferHgMax_Object((1,3,6,1,4,1,9,2,1,65),_BufferHgMax_Type())
bufferHgMax.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferHgMax.setStatus(_B)
_BufferHgHit_Type=Integer32
_BufferHgHit_Object=MibScalar
bufferHgHit=_BufferHgHit_Object((1,3,6,1,4,1,9,2,1,66),_BufferHgHit_Type())
bufferHgHit.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferHgHit.setStatus(_B)
_BufferHgMiss_Type=Integer32
_BufferHgMiss_Object=MibScalar
bufferHgMiss=_BufferHgMiss_Object((1,3,6,1,4,1,9,2,1,67),_BufferHgMiss_Type())
bufferHgMiss.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferHgMiss.setStatus(_B)
_BufferHgTrim_Type=Integer32
_BufferHgTrim_Object=MibScalar
bufferHgTrim=_BufferHgTrim_Object((1,3,6,1,4,1,9,2,1,68),_BufferHgTrim_Type())
bufferHgTrim.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferHgTrim.setStatus(_B)
_BufferHgCreate_Type=Integer32
_BufferHgCreate_Object=MibScalar
bufferHgCreate=_BufferHgCreate_Object((1,3,6,1,4,1,9,2,1,69),_BufferHgCreate_Type())
bufferHgCreate.setMaxAccess(_A)
if mibBuilder.loadTexts:bufferHgCreate.setStatus(_B)
mibBuilder.exportSymbols('OLD-CISCO-MEMORY-MIB',**{'lmem':lmem,'freeMem':freeMem,'bufferElFree':bufferElFree,'bufferElMax':bufferElMax,'bufferElHit':bufferElHit,'bufferElMiss':bufferElMiss,'bufferElCreate':bufferElCreate,'bufferSmSize':bufferSmSize,'bufferSmTotal':bufferSmTotal,'bufferSmFree':bufferSmFree,'bufferSmMax':bufferSmMax,'bufferSmHit':bufferSmHit,'bufferSmMiss':bufferSmMiss,'bufferSmTrim':bufferSmTrim,'bufferSmCreate':bufferSmCreate,'bufferMdSize':bufferMdSize,'bufferMdTotal':bufferMdTotal,'bufferMdFree':bufferMdFree,'bufferMdMax':bufferMdMax,'bufferMdHit':bufferMdHit,'bufferMdMiss':bufferMdMiss,'bufferMdTrim':bufferMdTrim,'bufferMdCreate':bufferMdCreate,'bufferBgSize':bufferBgSize,'bufferBgTotal':bufferBgTotal,'bufferBgFree':bufferBgFree,'bufferBgMax':bufferBgMax,'bufferBgHit':bufferBgHit,'bufferBgMiss':bufferBgMiss,'bufferBgTrim':bufferBgTrim,'bufferBgCreate':bufferBgCreate,'bufferLgSize':bufferLgSize,'bufferLgTotal':bufferLgTotal,'bufferLgFree':bufferLgFree,'bufferLgMax':bufferLgMax,'bufferLgHit':bufferLgHit,'bufferLgMiss':bufferLgMiss,'bufferLgTrim':bufferLgTrim,'bufferLgCreate':bufferLgCreate,'bufferFail':bufferFail,'bufferNoMem':bufferNoMem,'bufferHgSize':bufferHgSize,'bufferHgTotal':bufferHgTotal,'bufferHgFree':bufferHgFree,'bufferHgMax':bufferHgMax,'bufferHgHit':bufferHgHit,'bufferHgMiss':bufferHgMiss,'bufferHgTrim':bufferHgTrim,'bufferHgCreate':bufferHgCreate})