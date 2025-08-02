_L='scmCloningLastResult'
_K='scmCloningLastIPAddress'
_J='notSupportedCloning'
_I='versionMismatch'
_H='invalidFile'
_G='processing'
_F='completed'
_E='scmCloningIndex'
_D='SAMSUNG-CLONING-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hrDeviceIndex,=mibBuilder.importSymbols('HOST-RESOURCES-MIB','hrDeviceIndex')
samsungCommonMIB,=mibBuilder.importSymbols('SAMSUNG-COMMON-MIB','samsungCommonMIB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
scmCloningMIB=ModuleIdentity((1,3,6,1,4,1,236,11,5,11,82))
_ScmCloning_ObjectIdentity=ObjectIdentity
scmCloning=_ScmCloning_ObjectIdentity((1,3,6,1,4,1,236,11,5,11,82,1))
_ScmCloningTable_Object=MibTable
scmCloningTable=_ScmCloningTable_Object((1,3,6,1,4,1,236,11,5,11,82,1,1))
if mibBuilder.loadTexts:scmCloningTable.setStatus(_A)
_ScmCloningEntry_Object=MibTableRow
scmCloningEntry=_ScmCloningEntry_Object((1,3,6,1,4,1,236,11,5,11,82,1,1,1))
scmCloningEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:scmCloningEntry.setStatus(_A)
_ScmCloningIndex_Type=Integer32
_ScmCloningIndex_Object=MibTableColumn
scmCloningIndex=_ScmCloningIndex_Object((1,3,6,1,4,1,236,11,5,11,82,1,1,1,1),_ScmCloningIndex_Type())
scmCloningIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:scmCloningIndex.setStatus(_A)
_ScmCloningIPAddress_Type=IpAddress
_ScmCloningIPAddress_Object=MibTableColumn
scmCloningIPAddress=_ScmCloningIPAddress_Object((1,3,6,1,4,1,236,11,5,11,82,1,1,1,2),_ScmCloningIPAddress_Type())
scmCloningIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:scmCloningIPAddress.setStatus(_A)
class _ScmCloningResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5),('busy',6)))
_ScmCloningResult_Type.__name__=_C
_ScmCloningResult_Object=MibTableColumn
scmCloningResult=_ScmCloningResult_Object((1,3,6,1,4,1,236,11,5,11,82,1,1,1,3),_ScmCloningResult_Type())
scmCloningResult.setMaxAccess(_B)
if mibBuilder.loadTexts:scmCloningResult.setStatus(_A)
_ScmCloningDate_Type=OctetString
_ScmCloningDate_Object=MibTableColumn
scmCloningDate=_ScmCloningDate_Object((1,3,6,1,4,1,236,11,5,11,82,1,1,1,4),_ScmCloningDate_Type())
scmCloningDate.setMaxAccess(_B)
if mibBuilder.loadTexts:scmCloningDate.setStatus(_A)
_ScmCloningSimple_ObjectIdentity=ObjectIdentity
scmCloningSimple=_ScmCloningSimple_ObjectIdentity((1,3,6,1,4,1,236,11,5,11,82,1,2))
_ScmCloningLastIPAddress_Type=IpAddress
_ScmCloningLastIPAddress_Object=MibScalar
scmCloningLastIPAddress=_ScmCloningLastIPAddress_Object((1,3,6,1,4,1,236,11,5,11,82,1,2,1),_ScmCloningLastIPAddress_Type())
scmCloningLastIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:scmCloningLastIPAddress.setStatus(_A)
class _ScmCloningLastResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5),('busy',6)))
_ScmCloningLastResult_Type.__name__=_C
_ScmCloningLastResult_Object=MibScalar
scmCloningLastResult=_ScmCloningLastResult_Object((1,3,6,1,4,1,236,11,5,11,82,1,2,2),_ScmCloningLastResult_Type())
scmCloningLastResult.setMaxAccess(_B)
if mibBuilder.loadTexts:scmCloningLastResult.setStatus(_A)
_ScmCloningLastDate_Type=OctetString
_ScmCloningLastDate_Object=MibScalar
scmCloningLastDate=_ScmCloningLastDate_Object((1,3,6,1,4,1,236,11,5,11,82,1,2,3),_ScmCloningLastDate_Type())
scmCloningLastDate.setMaxAccess(_B)
if mibBuilder.loadTexts:scmCloningLastDate.setStatus(_A)
class _ScmCloningSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('supported',1),('notSupported',2)))
_ScmCloningSupported_Type.__name__=_C
_ScmCloningSupported_Object=MibScalar
scmCloningSupported=_ScmCloningSupported_Object((1,3,6,1,4,1,236,11,5,11,82,1,2,4),_ScmCloningSupported_Type())
scmCloningSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:scmCloningSupported.setStatus(_A)
_ScmCloningTrap_ObjectIdentity=ObjectIdentity
scmCloningTrap=_ScmCloningTrap_ObjectIdentity((1,3,6,1,4,1,236,11,5,11,82,1,3))
if mibBuilder.loadTexts:scmCloningTrap.setStatus(_A)
_ScmCloningTrapSimple_ObjectIdentity=ObjectIdentity
scmCloningTrapSimple=_ScmCloningTrapSimple_ObjectIdentity((1,3,6,1,4,1,236,11,5,11,82,1,3,1))
scmCloningTrapResult=NotificationType((1,3,6,1,4,1,236,11,5,11,82,1,3,1,1))
scmCloningTrapResult.setObjects(*((_D,_K),(_D,_L)))
if mibBuilder.loadTexts:scmCloningTrapResult.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'scmCloningMIB':scmCloningMIB,'scmCloning':scmCloning,'scmCloningTable':scmCloningTable,'scmCloningEntry':scmCloningEntry,_E:scmCloningIndex,'scmCloningIPAddress':scmCloningIPAddress,'scmCloningResult':scmCloningResult,'scmCloningDate':scmCloningDate,'scmCloningSimple':scmCloningSimple,_K:scmCloningLastIPAddress,_L:scmCloningLastResult,'scmCloningLastDate':scmCloningLastDate,'scmCloningSupported':scmCloningSupported,'scmCloningTrap':scmCloningTrap,'scmCloningTrapSimple':scmCloningTrapSimple,'scmCloningTrapResult':scmCloningTrapResult})