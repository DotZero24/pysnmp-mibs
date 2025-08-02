_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sonicwall=ModuleIdentity((1,3,6,1,4,1,8741))
if mibBuilder.loadTexts:sonicwall.setRevisions(('2017-01-06 00:00','2007-01-06 00:00'))
_SonicwallFw_ObjectIdentity=ObjectIdentity
sonicwallFw=_SonicwallFw_ObjectIdentity((1,3,6,1,4,1,8741,1))
if mibBuilder.loadTexts:sonicwallFw.setStatus(_A)
_SonicwallCommon_ObjectIdentity=ObjectIdentity
sonicwallCommon=_SonicwallCommon_ObjectIdentity((1,3,6,1,4,1,8741,2))
if mibBuilder.loadTexts:sonicwallCommon.setStatus(_A)
_SonicwallGMS_ObjectIdentity=ObjectIdentity
sonicwallGMS=_SonicwallGMS_ObjectIdentity((1,3,6,1,4,1,8741,3))
if mibBuilder.loadTexts:sonicwallGMS.setStatus(_A)
_SonicwallEmailSec_ObjectIdentity=ObjectIdentity
sonicwallEmailSec=_SonicwallEmailSec_ObjectIdentity((1,3,6,1,4,1,8741,4))
if mibBuilder.loadTexts:sonicwallEmailSec.setStatus(_A)
_SonicwallDataCenter_ObjectIdentity=ObjectIdentity
sonicwallDataCenter=_SonicwallDataCenter_ObjectIdentity((1,3,6,1,4,1,8741,5))
if mibBuilder.loadTexts:sonicwallDataCenter.setStatus(_A)
_SonicwallSSLVPN_ObjectIdentity=ObjectIdentity
sonicwallSSLVPN=_SonicwallSSLVPN_ObjectIdentity((1,3,6,1,4,1,8741,6))
if mibBuilder.loadTexts:sonicwallSSLVPN.setStatus(_A)
_SonicwallCDP_ObjectIdentity=ObjectIdentity
sonicwallCDP=_SonicwallCDP_ObjectIdentity((1,3,6,1,4,1,8741,7))
if mibBuilder.loadTexts:sonicwallCDP.setStatus(_A)
_SonicwallSMA_ObjectIdentity=ObjectIdentity
sonicwallSMA=_SonicwallSMA_ObjectIdentity((1,3,6,1,4,1,8741,8))
if mibBuilder.loadTexts:sonicwallSMA.setStatus(_A)
mibBuilder.exportSymbols('SONICWALL-SMI',**{'sonicwall':sonicwall,'sonicwallFw':sonicwallFw,'sonicwallCommon':sonicwallCommon,'sonicwallGMS':sonicwallGMS,'sonicwallEmailSec':sonicwallEmailSec,'sonicwallDataCenter':sonicwallDataCenter,'sonicwallSSLVPN':sonicwallSSLVPN,'sonicwallCDP':sonicwallCDP,'sonicwallSMA':sonicwallSMA})