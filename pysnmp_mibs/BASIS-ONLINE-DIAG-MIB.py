_H='boDiagGroup'
_G='diagTestId'
_F='diagResult'
_E='diagType'
_D='read-only'
_C='Integer32'
_B='BASIS-ONLINE-DIAG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
axisDiagnostics,=mibBuilder.importSymbols('BASIS-MIB','axisDiagnostics')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
basisOnlineDiagMIB=ModuleIdentity((1,3,6,1,4,1,351,150,80))
if mibBuilder.loadTexts:basisOnlineDiagMIB.setRevisions(('2003-06-11 00:00',))
_OnlineDiagnostics_ObjectIdentity=ObjectIdentity
onlineDiagnostics=_OnlineDiagnostics_ObjectIdentity((1,3,6,1,4,1,351,110,6,3))
class _DiagType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('post',1),('onlinediag',2)))
_DiagType_Type.__name__=_C
_DiagType_Object=MibScalar
diagType=_DiagType_Object((1,3,6,1,4,1,351,110,6,3,1),_DiagType_Type())
diagType.setMaxAccess(_D)
if mibBuilder.loadTexts:diagType.setStatus(_A)
class _DiagResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('passed',1),('failed',2)))
_DiagResult_Type.__name__=_C
_DiagResult_Object=MibScalar
diagResult=_DiagResult_Object((1,3,6,1,4,1,351,110,6,3,2),_DiagResult_Type())
diagResult.setMaxAccess(_D)
if mibBuilder.loadTexts:diagResult.setStatus(_A)
class _DiagTestId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DiagTestId_Type.__name__=_C
_DiagTestId_Object=MibScalar
diagTestId=_DiagTestId_Object((1,3,6,1,4,1,351,110,6,3,3),_DiagTestId_Type())
diagTestId.setMaxAccess(_D)
if mibBuilder.loadTexts:diagTestId.setStatus(_A)
_BoDiagMIBConformance_ObjectIdentity=ObjectIdentity
boDiagMIBConformance=_BoDiagMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,80,2))
_BoDiagMIBCompliances_ObjectIdentity=ObjectIdentity
boDiagMIBCompliances=_BoDiagMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,80,2,1))
_BoDiagMIBGroups_ObjectIdentity=ObjectIdentity
boDiagMIBGroups=_BoDiagMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,80,2,2))
boDiagGroup=ObjectGroup((1,3,6,1,4,1,351,150,80,2,2,1))
boDiagGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:boDiagGroup.setStatus(_A)
boDiagCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,80,2,1,1))
boDiagCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:boDiagCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'onlineDiagnostics':onlineDiagnostics,_E:diagType,_F:diagResult,_G:diagTestId,'basisOnlineDiagMIB':basisOnlineDiagMIB,'boDiagMIBConformance':boDiagMIBConformance,'boDiagMIBCompliances':boDiagMIBCompliances,'boDiagCompliance':boDiagCompliance,'boDiagMIBGroups':boDiagMIBGroups,_H:boDiagGroup})