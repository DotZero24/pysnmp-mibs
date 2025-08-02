_I='etsysAAAPolicyMgmtGroup'
_H='etsysAAAMgmtRemoteAcctProtocol'
_G='etsysAAAMgmtRemoteAuthProtocol'
_F='read-write'
_E='etsysAAAMgmtAccessProtocol'
_D='Integer32'
_C='AAAProtocol'
_B='ENTERASYS-AAA-POLICY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysAAAPolicyMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,51))
if mibBuilder.loadTexts:etsysAAAPolicyMIB.setRevisions(('2004-07-29 19:06',))
class AAAProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('any',1),('none',2),('radius',3),('tacacs',4)))
_EtsysAAAPolicyObjects_ObjectIdentity=ObjectIdentity
etsysAAAPolicyObjects=_EtsysAAAPolicyObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,51,1))
_EtsysAAAPolicyMgmtAccess_ObjectIdentity=ObjectIdentity
etsysAAAPolicyMgmtAccess=_EtsysAAAPolicyMgmtAccess_ObjectIdentity((1,3,6,1,4,1,5624,1,2,51,1,1))
_EtsysAAAMgmtAccessTable_Object=MibTable
etsysAAAMgmtAccessTable=_EtsysAAAMgmtAccessTable_Object((1,3,6,1,4,1,5624,1,2,51,1,1,1))
if mibBuilder.loadTexts:etsysAAAMgmtAccessTable.setStatus(_A)
_EtsysAAAMgmtAccessEntry_Object=MibTableRow
etsysAAAMgmtAccessEntry=_EtsysAAAMgmtAccessEntry_Object((1,3,6,1,4,1,5624,1,2,51,1,1,1,1))
etsysAAAMgmtAccessEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:etsysAAAMgmtAccessEntry.setStatus(_A)
class _EtsysAAAMgmtAccessProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('allProtocols',1))
_EtsysAAAMgmtAccessProtocol_Type.__name__=_D
_EtsysAAAMgmtAccessProtocol_Object=MibTableColumn
etsysAAAMgmtAccessProtocol=_EtsysAAAMgmtAccessProtocol_Object((1,3,6,1,4,1,5624,1,2,51,1,1,1,1,1),_EtsysAAAMgmtAccessProtocol_Type())
etsysAAAMgmtAccessProtocol.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:etsysAAAMgmtAccessProtocol.setStatus(_A)
class _EtsysAAAMgmtRemoteAuthProtocol_Type(AAAProtocol):defaultValue=1
_EtsysAAAMgmtRemoteAuthProtocol_Type.__name__=_C
_EtsysAAAMgmtRemoteAuthProtocol_Object=MibTableColumn
etsysAAAMgmtRemoteAuthProtocol=_EtsysAAAMgmtRemoteAuthProtocol_Object((1,3,6,1,4,1,5624,1,2,51,1,1,1,1,2),_EtsysAAAMgmtRemoteAuthProtocol_Type())
etsysAAAMgmtRemoteAuthProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysAAAMgmtRemoteAuthProtocol.setStatus(_A)
class _EtsysAAAMgmtRemoteAcctProtocol_Type(AAAProtocol):defaultValue=1
_EtsysAAAMgmtRemoteAcctProtocol_Type.__name__=_C
_EtsysAAAMgmtRemoteAcctProtocol_Object=MibTableColumn
etsysAAAMgmtRemoteAcctProtocol=_EtsysAAAMgmtRemoteAcctProtocol_Object((1,3,6,1,4,1,5624,1,2,51,1,1,1,1,3),_EtsysAAAMgmtRemoteAcctProtocol_Type())
etsysAAAMgmtRemoteAcctProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysAAAMgmtRemoteAcctProtocol.setStatus(_A)
_EtsysAAAPolicyMIBConformance_ObjectIdentity=ObjectIdentity
etsysAAAPolicyMIBConformance=_EtsysAAAPolicyMIBConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,51,2))
_EtsysAAAPolicyMIBCompliances_ObjectIdentity=ObjectIdentity
etsysAAAPolicyMIBCompliances=_EtsysAAAPolicyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,51,2,1))
_EtsysAAAPolicyMIBGroups_ObjectIdentity=ObjectIdentity
etsysAAAPolicyMIBGroups=_EtsysAAAPolicyMIBGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,51,2,2))
etsysAAAPolicyMgmtGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,51,2,2,1))
etsysAAAPolicyMgmtGroup.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:etsysAAAPolicyMgmtGroup.setStatus(_A)
etsysAAAPolicyMIBCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,51,2,1,1))
etsysAAAPolicyMIBCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:etsysAAAPolicyMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_C:AAAProtocol,'etsysAAAPolicyMIB':etsysAAAPolicyMIB,'etsysAAAPolicyObjects':etsysAAAPolicyObjects,'etsysAAAPolicyMgmtAccess':etsysAAAPolicyMgmtAccess,'etsysAAAMgmtAccessTable':etsysAAAMgmtAccessTable,'etsysAAAMgmtAccessEntry':etsysAAAMgmtAccessEntry,_E:etsysAAAMgmtAccessProtocol,_G:etsysAAAMgmtRemoteAuthProtocol,_H:etsysAAAMgmtRemoteAcctProtocol,'etsysAAAPolicyMIBConformance':etsysAAAPolicyMIBConformance,'etsysAAAPolicyMIBCompliances':etsysAAAPolicyMIBCompliances,'etsysAAAPolicyMIBCompliance':etsysAAAPolicyMIBCompliance,'etsysAAAPolicyMIBGroups':etsysAAAPolicyMIBGroups,_I:etsysAAAPolicyMgmtGroup})