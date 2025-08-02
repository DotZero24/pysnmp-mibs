_F='read-write'
_E='Unsigned32'
_D='fsErpsRingId'
_C='fsErpsContextId'
_B='ARICENT-ERPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsErpsContextId,fsErpsRingId=mibBuilder.importSymbols(_B,_C,_D)
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
eltMesIssErpsMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,29))
if mibBuilder.loadTexts:eltMesIssErpsMIB.setRevisions(('2021-12-06 00:00',))
_EltMesIssErpsObjects_ObjectIdentity=ObjectIdentity
eltMesIssErpsObjects=_EltMesIssErpsObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,29,1))
_EltMesIssErpsRingConfig_ObjectIdentity=ObjectIdentity
eltMesIssErpsRingConfig=_EltMesIssErpsRingConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,139,29,1,1))
_EltMesIssErpsRingIfmTable_Object=MibTable
eltMesIssErpsRingIfmTable=_EltMesIssErpsRingIfmTable_Object((1,3,6,1,4,1,35265,1,139,29,1,1,2))
if mibBuilder.loadTexts:eltMesIssErpsRingIfmTable.setStatus(_A)
_EltMesIssErpsRingIfmEntry_Object=MibTableRow
eltMesIssErpsRingIfmEntry=_EltMesIssErpsRingIfmEntry_Object((1,3,6,1,4,1,35265,1,139,29,1,1,2,1))
eltMesIssErpsRingIfmEntry.setIndexNames((0,_B,_C),(0,_B,_D))
if mibBuilder.loadTexts:eltMesIssErpsRingIfmEntry.setStatus(_A)
class _EltMesIssErpsRingIfmMdLevel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_EltMesIssErpsRingIfmMdLevel_Type.__name__=_E
_EltMesIssErpsRingIfmMdLevel_Object=MibTableColumn
eltMesIssErpsRingIfmMdLevel=_EltMesIssErpsRingIfmMdLevel_Object((1,3,6,1,4,1,35265,1,139,29,1,1,2,1,1),_EltMesIssErpsRingIfmMdLevel_Type())
eltMesIssErpsRingIfmMdLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssErpsRingIfmMdLevel.setStatus(_A)
_EltMesIssErpsRingIfmRowStatus_Type=RowStatus
_EltMesIssErpsRingIfmRowStatus_Object=MibTableColumn
eltMesIssErpsRingIfmRowStatus=_EltMesIssErpsRingIfmRowStatus_Object((1,3,6,1,4,1,35265,1,139,29,1,1,2,1,2),_EltMesIssErpsRingIfmRowStatus_Type())
eltMesIssErpsRingIfmRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssErpsRingIfmRowStatus.setStatus(_A)
mibBuilder.exportSymbols('ELTEX-MES-ISS-ERPS-MIB',**{'eltMesIssErpsMIB':eltMesIssErpsMIB,'eltMesIssErpsObjects':eltMesIssErpsObjects,'eltMesIssErpsRingConfig':eltMesIssErpsRingConfig,'eltMesIssErpsRingIfmTable':eltMesIssErpsRingIfmTable,'eltMesIssErpsRingIfmEntry':eltMesIssErpsRingIfmEntry,'eltMesIssErpsRingIfmMdLevel':eltMesIssErpsRingIfmMdLevel,'eltMesIssErpsRingIfmRowStatus':eltMesIssErpsRingIfmRowStatus})