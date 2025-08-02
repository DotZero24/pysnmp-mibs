_J='apAMISoapHttpsPort'
_I='apAMISoapHttps'
_H='apAMISoapHttpPort'
_G='apAMISoapHttp'
_F='disabled'
_E='enabled'
_D='Integer32'
_C='read-only'
_B='APAMI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acmepacketMgmt,=mibBuilder.importSymbols('ACMEPACKET-SMI','acmepacketMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
apAMIModule=ModuleIdentity((1,3,6,1,4,1,9148,3,6))
if mibBuilder.loadTexts:apAMIModule.setRevisions(('2012-07-16 00:00',))
_ApAMIMIBObjects_ObjectIdentity=ObjectIdentity
apAMIMIBObjects=_ApAMIMIBObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,6,1))
_ApAMISoapObjects_ObjectIdentity=ObjectIdentity
apAMISoapObjects=_ApAMISoapObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,6,1,1))
class _ApAMISoapHttp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ApAMISoapHttp_Type.__name__=_D
_ApAMISoapHttp_Object=MibScalar
apAMISoapHttp=_ApAMISoapHttp_Object((1,3,6,1,4,1,9148,3,6,1,1,1),_ApAMISoapHttp_Type())
apAMISoapHttp.setMaxAccess(_C)
if mibBuilder.loadTexts:apAMISoapHttp.setStatus(_A)
_ApAMISoapHttpPort_Type=Integer32
_ApAMISoapHttpPort_Object=MibScalar
apAMISoapHttpPort=_ApAMISoapHttpPort_Object((1,3,6,1,4,1,9148,3,6,1,1,2),_ApAMISoapHttpPort_Type())
apAMISoapHttpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:apAMISoapHttpPort.setStatus(_A)
class _ApAMISoapHttps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ApAMISoapHttps_Type.__name__=_D
_ApAMISoapHttps_Object=MibScalar
apAMISoapHttps=_ApAMISoapHttps_Object((1,3,6,1,4,1,9148,3,6,1,1,3),_ApAMISoapHttps_Type())
apAMISoapHttps.setMaxAccess(_C)
if mibBuilder.loadTexts:apAMISoapHttps.setStatus(_A)
_ApAMISoapHttpsPort_Type=Integer32
_ApAMISoapHttpsPort_Object=MibScalar
apAMISoapHttpsPort=_ApAMISoapHttpsPort_Object((1,3,6,1,4,1,9148,3,6,1,1,4),_ApAMISoapHttpsPort_Type())
apAMISoapHttpsPort.setMaxAccess(_C)
if mibBuilder.loadTexts:apAMISoapHttpsPort.setStatus(_A)
_ApAMIModuleConformance_ObjectIdentity=ObjectIdentity
apAMIModuleConformance=_ApAMIModuleConformance_ObjectIdentity((1,3,6,1,4,1,9148,3,6,2))
_ApAMIModuleGroups_ObjectIdentity=ObjectIdentity
apAMIModuleGroups=_ApAMIModuleGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,6,2,1))
apAMIMibObjectsGroup=ObjectGroup((1,3,6,1,4,1,9148,3,6,2,1,1))
apAMIMibObjectsGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:apAMIMibObjectsGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'apAMIModule':apAMIModule,'apAMIMIBObjects':apAMIMIBObjects,'apAMISoapObjects':apAMISoapObjects,_G:apAMISoapHttp,_H:apAMISoapHttpPort,_I:apAMISoapHttps,_J:apAMISoapHttpsPort,'apAMIModuleConformance':apAMIModuleConformance,'apAMIModuleGroups':apAMIModuleGroups,'apAMIMibObjectsGroup':apAMIMibObjectsGroup})