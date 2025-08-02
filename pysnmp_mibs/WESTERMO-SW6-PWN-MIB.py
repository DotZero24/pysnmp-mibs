_H='groupCfgWlanBandsteering'
_G='cfgWlanBsteerMatchingSsid'
_F='cfgWlanBsteerEnabled'
_E='read-write'
_D='DisplayString'
_C='Integer32'
_B='WESTERMO-SW6-PWN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
pwn=ModuleIdentity((1,3,6,1,4,1,16177,1,400,2,9))
if mibBuilder.loadTexts:pwn.setRevisions(('2019-09-06 00:00',))
_Configuration_ObjectIdentity=ObjectIdentity
configuration=_Configuration_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,9,1))
_CfgWireless_ObjectIdentity=ObjectIdentity
cfgWireless=_CfgWireless_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,9,1,1))
_CfgWlanBandsteering_ObjectIdentity=ObjectIdentity
cfgWlanBandsteering=_CfgWlanBandsteering_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,9,1,1,1))
class _CfgWlanBsteerEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_CfgWlanBsteerEnabled_Type.__name__=_C
_CfgWlanBsteerEnabled_Object=MibScalar
cfgWlanBsteerEnabled=_CfgWlanBsteerEnabled_Object((1,3,6,1,4,1,16177,1,400,2,9,1,1,1,1),_CfgWlanBsteerEnabled_Type())
cfgWlanBsteerEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:cfgWlanBsteerEnabled.setStatus(_A)
class _CfgWlanBsteerMatchingSsid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CfgWlanBsteerMatchingSsid_Type.__name__=_D
_CfgWlanBsteerMatchingSsid_Object=MibScalar
cfgWlanBsteerMatchingSsid=_CfgWlanBsteerMatchingSsid_Object((1,3,6,1,4,1,16177,1,400,2,9,1,1,1,2),_CfgWlanBsteerMatchingSsid_Type())
cfgWlanBsteerMatchingSsid.setMaxAccess(_E)
if mibBuilder.loadTexts:cfgWlanBsteerMatchingSsid.setStatus(_A)
_Conformance_ObjectIdentity=ObjectIdentity
conformance=_Conformance_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,9,10000))
_Groups_ObjectIdentity=ObjectIdentity
groups=_Groups_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,9,10000,1))
_GroupConfiguration_ObjectIdentity=ObjectIdentity
groupConfiguration=_GroupConfiguration_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,9,10000,1,1))
_Compliances_ObjectIdentity=ObjectIdentity
compliances=_Compliances_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,9,10000,2))
groupCfgWlanBandsteering=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,9,10000,1,1,1))
groupCfgWlanBandsteering.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:groupCfgWlanBandsteering.setStatus(_A)
compliance=ModuleCompliance((1,3,6,1,4,1,16177,1,400,2,9,10000,2,1))
compliance.setObjects((_B,_H))
if mibBuilder.loadTexts:compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pwn':pwn,'configuration':configuration,'cfgWireless':cfgWireless,'cfgWlanBandsteering':cfgWlanBandsteering,_F:cfgWlanBsteerEnabled,_G:cfgWlanBsteerMatchingSsid,'conformance':conformance,'groups':groups,'groupConfiguration':groupConfiguration,_H:groupCfgWlanBandsteering,'compliances':compliances,'compliance':compliance})