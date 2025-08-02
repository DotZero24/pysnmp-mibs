_E='read-write'
_D='read-only'
_C='ctZiplockNumber'
_B='ZIPLOCK-MIB'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctResource,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctResource')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtZiplock_ObjectIdentity=ObjectIdentity
ctZiplock=_CtZiplock_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,12,3))
_CtZiplockTable_Object=MibTable
ctZiplockTable=_CtZiplockTable_Object((1,3,6,1,4,1,52,4,1,1,12,3,1))
if mibBuilder.loadTexts:ctZiplockTable.setStatus(_A)
_CtZiplockEntry_Object=MibTableRow
ctZiplockEntry=_CtZiplockEntry_Object((1,3,6,1,4,1,52,4,1,1,12,3,1,1))
ctZiplockEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:ctZiplockEntry.setStatus(_A)
_CtZiplockNumber_Type=Integer32
_CtZiplockNumber_Object=MibTableColumn
ctZiplockNumber=_CtZiplockNumber_Object((1,3,6,1,4,1,52,4,1,1,12,3,1,1,1),_CtZiplockNumber_Type())
ctZiplockNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:ctZiplockNumber.setStatus(_A)
_CtZiplockPresence_Type=Integer32
_CtZiplockPresence_Object=MibTableColumn
ctZiplockPresence=_CtZiplockPresence_Object((1,3,6,1,4,1,52,4,1,1,12,3,1,1,2),_CtZiplockPresence_Type())
ctZiplockPresence.setMaxAccess(_D)
if mibBuilder.loadTexts:ctZiplockPresence.setStatus(_A)
_CtZiplockRevision_Type=Integer32
_CtZiplockRevision_Object=MibTableColumn
ctZiplockRevision=_CtZiplockRevision_Object((1,3,6,1,4,1,52,4,1,1,12,3,1,1,3),_CtZiplockRevision_Type())
ctZiplockRevision.setMaxAccess(_E)
if mibBuilder.loadTexts:ctZiplockRevision.setStatus(_A)
_CtZiplockStatus_Type=Integer32
_CtZiplockStatus_Object=MibTableColumn
ctZiplockStatus=_CtZiplockStatus_Object((1,3,6,1,4,1,52,4,1,1,12,3,1,1,4),_CtZiplockStatus_Type())
ctZiplockStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ctZiplockStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ctZiplock':ctZiplock,'ctZiplockTable':ctZiplockTable,'ctZiplockEntry':ctZiplockEntry,_C:ctZiplockNumber,'ctZiplockPresence':ctZiplockPresence,'ctZiplockRevision':ctZiplockRevision,'ctZiplockStatus':ctZiplockStatus})